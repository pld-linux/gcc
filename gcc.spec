#
# TODO:
# - gconf peer? (but libgcj needs split anyway)
# - package?
#   /usr/bin/aot-compile                                                                                                                                    
#   /usr/bin/gjdoc
#   /usr/share/man/man1/aot-compile.1.gz
#   /usr/share/man/man1/gjdoc.1.gz
#   /usr/share/python/aotcompile.py
#   /usr/share/python/classfile.py
#
# Conditional build:
%bcond_without	ada		# build without ADA support
%bcond_without	cxx		# build without C++ support
%bcond_without	fortran		# build without Fortran support
%bcond_without	gomp		# build without OpenMP support
%bcond_without	java		# build without Java support
%bcond_without	mudflap		# build without Mudflap pointer debugging support
%bcond_without	objc		# build without Objective-C support
%bcond_without	objcxx		# build without Objective-C++ support
%bcond_without	alsa		# don't build libgcj ALSA MIDI interface
%bcond_without	dssi		# don't build libgcj DSSI MIDI interface
%bcond_without	gtk		# don't build libgcj GTK peer
%bcond_without	mozilla		# don't build libgcjwebplugin
%bcond_with	qt		# build libgcj Qt peer (currently doesn't build with libtool-2.x)
%bcond_without	x		# don't build libgcj Xlib-dependent AWTs (incl. GTK/Qt)
%bcond_without	multilib	# build without multilib support (it needs glibc[32&64]-devel)
%bcond_with	profiling	# build with profiling
%bcond_without	bootstrap	# omit 3-stage bootstrap
%bcond_with	tests		# torture gcc

%if %{without cxx}
%undefine	with_java
%undefine	with_objcxx
%endif

%if %{without objc}
%undefine	with_objcxx
%endif

%if %{without bootstrap}
%undefine	with_profiling
%endif

%if %{without x}
%undefine	with_gtk
%undefine	with_qt
%endif

%ifnarch %{x8664} ppc64 s390x sparc64
%undefine	with_multilib
%endif

%ifarch sparc64
%undefine	with_ada
%endif

%define		major_ver	4.4
%define		minor_ver	0
# class data version seen with file(1) that this jvm is able to load
%define		_classdataversion 50.0

Summary:	GNU Compiler Collection: the C compiler and shared files
Summary(es.UTF-8):	Colección de compiladores GNU: el compilador C y ficheros compartidos
Summary(pl.UTF-8):	Kolekcja kompilatorów GNU: kompilator C i pliki współdzielone
Summary(pt_BR.UTF-8):	Coleção dos compiladores GNU: o compilador C e arquivos compartilhados
Name:		gcc
Version:	%{major_ver}.%{minor_ver}
Release:	6
Epoch:		6
License:	GPL v3+
Group:		Development/Languages
Source0:	ftp://gcc.gnu.org/pub/gcc/releases/gcc-%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	cf5d787bee57f38168b74d65a7c0e6fd
Source1:	%{name}-optimize-la.pl
#Source2:	ftp://sourceware.org/pub/java/ecj-%{major_ver}.jar
Source2:	ftp://sourceware.org/pub/java/ecj-latest.jar
# Source2-md5:	fd299f26c02268878b5d6c0e86f57c43
# svn diff svn://gcc.gnu.org/svn/gcc//tags/gcc_4_4_0_release svn://gcc.gnu.org/svn/gcc/branches/gcc-4_4-branch > gcc-branch.diff
Patch100:	%{name}-branch.diff
# svn diff svn://gcc.gnu.org/svn/gcc/branches/gcc-4_4-branch@??? svn://gcc.gnu.org/svn/gcc/branches/ix86/gcc-4_4-branch > gcc-ix86-branch.diff
# The goal of this ix86-branch is to add support for newer ix86 processors such as AMD's Shanghai and Intel's Atom to GCC 4.4.x.
Patch101:	%{name}-ix86-branch.diff
Patch0:		%{name}-info.patch
Patch1:		%{name}-nolocalefiles.patch
Patch2:		%{name}-nodebug.patch
Patch3:		%{name}-ada-link.patch
Patch4:		%{name}-sparc64-ada_fix.patch
Patch5:		%{name}-pr14912.patch
Patch6:		%{name}-ppc64-m32-m64-multilib-only.patch
Patch7:		%{name}-libjava-multilib.patch
Patch8:		%{name}-enable-java-awt-qt.patch
Patch9:		%{name}-hash-style-gnu.patch
Patch10:	%{name}-moresparcs.patch
Patch11:	%{name}-build-id.patch
URL:		http://gcc.gnu.org/
BuildRequires:	autoconf
%{?with_tests:BuildRequires:	autogen}
BuildRequires:	automake
# binutils 2.17.50.0.9 or newer are required for fixing PR middle-end/20218.
BuildRequires:	binutils >= 2:2.17.50.0.9-1
BuildRequires:	bison
BuildRequires:	chrpath >= 0.13-2
%{?with_tests:BuildRequires:	dejagnu}
BuildRequires:	fileutils >= 4.0.41
BuildRequires:	flex
%if %{with ada}
BuildRequires:	gcc(ada)
BuildRequires:	gcc-ada
%endif
BuildRequires:	gettext-devel
BuildRequires:	glibc-devel >= 6:2.4-1
%if %{with multilib}
BuildRequires:	gcc(multilib)
%ifarch %{x8664}
BuildRequires:	glibc-devel(i686)
%endif
%ifarch ppc64
BuildRequires:	glibc-devel(ppc)
%endif
%ifarch s390x
BuildRequires:	glibc-devel(s390)
%endif
%ifarch sparc64
BuildRequires:	glibc-devel(sparcv9)
%endif
%endif
BuildRequires:	gmp-devel >= 4.1
BuildRequires:	mpfr-devel >= 2.3.0
BuildRequires:	rpmbuild(macros) >= 1.211
BuildRequires:	texinfo >= 4.1
BuildRequires:	zlib-devel
%if %{with java}
%{?with_alsa:BuildRequires:	alsa-lib-devel}
%if %{with dssi}
BuildRequires:	dssi
BuildRequires:	jack-audio-connection-kit-devel
%endif
BuildRequires:	libxml2-devel >= 1:2.6.8
BuildRequires:	libxslt-devel >= 1.1.11
BuildRequires:	perl-base
BuildRequires:	perl-tools-pod
BuildRequires:	pkgconfig
BuildRequires:	unzip
BuildRequires:	zip
%if %{with gtk}
BuildRequires:	cairo-devel >= 0.5.0
BuildRequires:	gtk+2-devel >= 2:2.4.0
BuildRequires:	libart_lgpl-devel
BuildRequires:	pango-devel
BuildRequires:	xorg-lib-libXtst-devel
%endif
%if %{with qt}
BuildRequires:	QtGui-devel >= 4.0.1
BuildRequires:	qt4-build >= 4.0.1
%endif
%{?with_mozilla:BuildRequires:	xulrunner-devel >= 1.8.1.3-1.20070321.5}
%endif
Requires:	binutils >= 2:2.17.50.0.9-1
Requires:	libgcc = %{epoch}:%{version}-%{release}
Provides:	cpp = %{epoch}:%{version}-%{release}
%{?with_ada:Provides:	gcc(ada)}
Obsoletes:	cpp
Obsoletes:	egcs-cpp
Obsoletes:	gcc-chill
Obsoletes:	gcc-cpp
Obsoletes:	gcc-ksi
Obsoletes:	gcc4
Obsoletes:	gont
Conflicts:	glibc-devel < 2.2.5-20
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_slibdir	/%{_lib}
%if %{with multilib}
# 32-bit environment on x86-64,ppc64,s390x,sparc64
%define		_slibdir32	/lib
%define		_libdir32	/usr/lib
%endif

%define		filterout	-fwrapv -fno-strict-aliasing -fsigned-char
%define		filterout_ld	-Wl,--as-needed

%description
A compiler aimed at integrating all the optimizations and features
necessary for a high-performance and stable development environment.

This package contains the C compiler and some files shared by various
parts of the GNU Compiler Collection. In order to use another GCC
compiler you will need to install the appropriate subpackage.

%description -l es.UTF-8
Un compilador que intenta integrar todas las optimalizaciones y
características necesarias para un entorno de desarrollo eficaz y
estable.

Este paquete contiene el compilador de C y unos ficheros compartidos
por varias partes de la colección de compiladores GNU (GCC). Para usar
otro compilador de GCC será necesario que instale el subpaquete
adecuado.

%description -l pl.UTF-8
Kompilator, posiadający duże możliwości optymalizacyjne niezbędne do
wyprodukowania szybkiego i stabilnego kodu wynikowego.

Ten pakiet zawiera kompilator C i pliki współdzielone przez różne
części kolekcji kompilatorów GNU (GCC). Żeby używać innego kompilatora
z GCC, trzeba zainstalować odpowiedni podpakiet.

%description -l pt_BR.UTF-8
Este pacote adiciona infraestrutura básica e suporte a linguagem C ao
GNU Compiler Collection.

%package multilib
Summary:	GNU Compiler Collection: the C compiler and shared files
Summary(es.UTF-8):	Colección de compiladores GNU: el compilador C y ficheros compartidos
Summary(pl.UTF-8):	Kolekcja kompilatorów GNU: kompilator C i pliki współdzielone
Summary(pt_BR.UTF-8):	Coleção dos compiladores GNU: o compilador C e arquivos compartilhados
License:	GPL v3+
Group:		Development/Languages
Requires:	%{name}
Requires:	libgcc-multilib = %{epoch}:%{version}-%{release}
%{?with_multilib:Provides:      gcc(multilib)}
Obsoletes:	libgcc32
%ifarch %{x8664}
Requires:	glibc-devel(i686)
%endif
%ifarch ppc64
Requires:	glibc-devel(ppc)
%endif
%ifarch s390x
Requires:	glibc-devel(s390)
%endif
%ifarch sparc64
Requires:	glibc-devel(sparc)
%endif

%description multilib
A compiler aimed at integrating all the optimizations and features
necessary for a high-performance and stable development environment.

This package contains the C compiler and some files shared by various
parts of the GNU Compiler Collection. In order to use another GCC
compiler you will need to install the appropriate subpackage.

%description multilib -l es.UTF-8
Un compilador que intenta integrar todas las optimalizaciones y
características necesarias para un entorno de desarrollo eficaz y
estable.

Este paquete contiene el compilador de C y unos ficheros compartidos
por varias partes de la colección de compiladores GNU (GCC). Para usar
otro compilador de GCC será necesario que instale el subpaquete
adecuado.

%description multilib -l pl.UTF-8
Kompilator, posiadający duże możliwości optymalizacyjne niezbędne do
wyprodukowania szybkiego i stabilnego kodu wynikowego.

Ten pakiet zawiera kompilator C i pliki współdzielone przez różne
części kolekcji kompilatorów GNU (GCC). Żeby używać innego kompilatora
z GCC, trzeba zainstalować odpowiedni podpakiet.

%description multilib -l pt_BR.UTF-8
Este pacote adiciona infraestrutura básica e suporte a linguagem C ao
GNU Compiler Collection.

%package -n libgcc
Summary:	Shared gcc library
Summary(es.UTF-8):	Biblioteca compartida de gcc
Summary(pl.UTF-8):	Biblioteka gcc
Summary(pt_BR.UTF-8):	Biblioteca runtime para o GCC
License:	GPL v2+ with unlimited link permission
Group:		Libraries
Obsoletes:	libgcc1
Obsoletes:	libgcc4

%description -n libgcc
Shared gcc library.

%description -n libgcc -l es.UTF-8
Biblioteca compartida de gcc.

%description -n libgcc -l pl.UTF-8
Biblioteka dynamiczna gcc.

%description -n libgcc -l pt_BR.UTF-8
Biblioteca runtime para o GCC.

%package -n libgcc-multilib
Summary:	Shared gcc library
Summary(es.UTF-8):	Biblioteca compartida de gcc
Summary(pl.UTF-8):	Biblioteka gcc
Summary(pt_BR.UTF-8):	Biblioteca runtime para o GCC
License:	GPL v2+ with unlimited link permission
Group:		Libraries

%description -n libgcc-multilib
Shared gcc library.

%description -n libgcc-multilib -l es.UTF-8
Biblioteca compartida de gcc.

%description -n libgcc-multilib -l pl.UTF-8
Biblioteka dynamiczna gcc.

%description -n libgcc-multilib -l pt_BR.UTF-8
Biblioteca runtime para o GCC.

%package -n libgomp
Summary:	GNU OpenMP library
Summary(pl.UTF-8):	Biblioteka GNU OpenMP
License:	LGPL v2.1+ with unlimited link permission
Group:		Libraries

%description -n libgomp
GNU OpenMP library.

%description -n libgomp -l pl.UTF-8
Biblioteka GNU OpenMP.

%package -n libgomp-multilib
Summary:	GNU OpenMP library
Summary(pl.UTF-8):	Biblioteka GNU OpenMP
License:	LGPL v2.1+ with unlimited link permission
Group:		Libraries

%description -n libgomp-multilib
GNU OpenMP library.

%description -n libgomp-multilib -l pl.UTF-8
Biblioteka GNU OpenMP.

%package -n libgomp-devel
Summary:	Development files for GNU OpenMP library
Summary(pl.UTF-8):	Pliki programistyczne biblioteki GNU OpenMP
License:	LGPL v2.1+ with unlimited link permission
Group:		Development/Libraries
Requires:	libgomp = %{epoch}:%{version}-%{release}

%description -n libgomp-devel
Development files for GNU OpenMP library.

%description -n libgomp-devel -l pl.UTF-8
Pliki programistyczne biblioteki GNU OpenMP.

%package -n libgomp-multilib-devel
Summary:	Development files for GNU OpenMP library
Summary(pl.UTF-8):	Pliki programistyczne biblioteki GNU OpenMP
License:	LGPL v2.1+ with unlimited link permission
Group:		Development/Libraries
Requires:	libgomp-devel = %{epoch}:%{version}-%{release}

%description -n libgomp-multilib-devel
Development files for GNU OpenMP library.

%description -n libgomp-multilib-devel -l pl.UTF-8
Pliki programistyczne biblioteki GNU OpenMP.

%package -n libgomp-static
Summary:	Static GNU OpenMP library
Summary(pl.UTF-8):	Statyczna biblioteka GNU OpenMP
License:	LGPL v2.1+ with unlimited link permission
Group:		Development/Libraries
Requires:	libgomp-devel = %{epoch}:%{version}-%{release}

%description -n libgomp-static
Static GNU OpenMP library.

%description -n libgomp-static -l pl.UTF-8
Statyczna biblioteka GNU OpenMP.

%package -n libgomp-multilib-static
Summary:	Static GNU OpenMP library
Summary(pl.UTF-8):	Statyczna biblioteka GNU OpenMP
License:	LGPL v2.1+ with unlimited link permission
Group:		Development/Libraries
Requires:	libgomp-multilib-devel

%description -n libgomp-multilib-static
Static GNU OpenMP library.

%description -n libgomp-multilib-static -l pl.UTF-8
Statyczna biblioteka GNU OpenMP.

%package -n libmudflap
Summary:	GCC mudflap shared support library
Summary(pl.UTF-8):	Współdzielona biblioteka wspomagająca GCC mudflap
License:	GPL v2+ with unlimited link permission
Group:		Libraries

%description -n libmudflap
The libmudflap libraries are used by GCC for instrumenting pointer and
array dereferencing operations.

%description -n libmudflap -l pl.UTF-8
Biblioteki libmudflap są używane przez GCC do obsługi operacji
dereferencji wspaźników i tablic.

%package -n libmudflap-multilib
Summary:	GCC mudflap shared support library
Summary(pl.UTF-8):	Współdzielona biblioteka wspomagająca GCC mudflap
License:	GPL v2+ with unlimited link permission
Group:		Libraries

%description -n libmudflap-multilib
The libmudflap libraries are used by GCC for instrumenting pointer and
array dereferencing operations.

%description -n libmudflap-multilib -l pl.UTF-8
Biblioteki libmudflap są używane przez GCC do obsługi operacji
dereferencji wspaźników i tablic.

%package -n libmudflap-devel
Summary:	Development files for GCC mudflap library
Summary(pl.UTF-8):	Pliki programistyczne biblioteki GCC mudflap
License:	GPL v2+ with unlimited link permission
Group:		Development/Libraries
Requires:	libmudflap = %{epoch}:%{version}-%{release}

%description -n libmudflap-devel
The libmudflap libraries are used by GCC for instrumenting pointer and
array dereferencing operations. This package contains development
files.

%description -n libmudflap-devel -l pl.UTF-8
Biblioteki libmudflap są używane przez GCC do obsługi operacji
dereferencji wspaźników i tablic. Ten pakiet zawiera pliki
programistyczne.

%package -n libmudflap-multilib-devel
Summary:	Development files for GCC mudflap library
Summary(pl.UTF-8):	Pliki programistyczne biblioteki GCC mudflap
License:	GPL v2+ with unlimited link permission
Group:		Development/Libraries
Requires:	libmudflap-devel = %{epoch}:%{version}-%{release}

%description -n libmudflap-multilib-devel
The libmudflap libraries are used by GCC for instrumenting pointer and
array dereferencing operations. This package contains development
files.

%description -n libmudflap-multilib-devel -l pl.UTF-8
Biblioteki libmudflap są używane przez GCC do obsługi operacji
dereferencji wspaźników i tablic. Ten pakiet zawiera pliki
programistyczne.

%package -n libmudflap-static
Summary:	Static GCC mudflap library
Summary(pl.UTF-8):	Statyczna biblioteka GCC mudflap
License:	GPL v2+ with unlimited link permission
Group:		Development/Libraries
Requires:	libmudflap-devel = %{epoch}:%{version}-%{release}

%description -n libmudflap-static
The libmudflap libraries are used by GCC for instrumenting pointer and
array dereferencing operations. This package contains static
libraries.

%description -n libmudflap-static -l pl.UTF-8
Biblioteki libmudflap są używane przez GCC do obsługi operacji
dereferencji wspaźników i tablic. Ten pakiet zawiera biblioteki
statyczne.

%package -n libmudflap-multilib-static
Summary:	Static GCC mudflap library
Summary(pl.UTF-8):	Statyczna biblioteka GCC mudflap
License:	GPL v2+ with unlimited link permission
Group:		Development/Libraries
Requires:	libmudflap-multilib-devel

%description -n libmudflap-multilib-static
The libmudflap libraries are used by GCC for instrumenting pointer and
array dereferencing operations. This package contains static
libraries.

%description -n libmudflap-multilib-static -l pl.UTF-8
Biblioteki libmudflap są używane przez GCC do obsługi operacji
dereferencji wspaźników i tablic. Ten pakiet zawiera biblioteki
statyczne.

%package ada
Summary:	Ada support for gcc
Summary(es.UTF-8):	Soporte de Ada para gcc
Summary(pl.UTF-8):	Obsługa Ady do gcc
Group:		Development/Languages
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	libgnat = %{epoch}:%{version}-%{release}
Obsoletes:	gcc-gnat
Obsoletes:	gnat-devel

%description ada
This package adds experimental support for compiling Ada programs.

%description ada -l es.UTF-8
Este paquete añade soporte experimental para compilar programas en
Ada.

%description ada -l pl.UTF-8
Ten pakiet dodaje eksperymentalne wsparcie dla kompilacji programów w
Adzie.

%package ada-multilib
Summary:	Ada support for gcc
Summary(es.UTF-8):	Soporte de Ada para gcc
Summary(pl.UTF-8):	Obsługa Ady do gcc
Group:		Development/Languages
Requires:	%{name}-ada = %{epoch}:%{version}-%{release}
Requires:	libgnat-multilib = %{epoch}:%{version}-%{release}

%description ada-multilib
This package adds experimental support for compiling Ada programs.

%description ada-multilib -l es.UTF-8
Este paquete añade soporte experimental para compilar programas en
Ada.

%description ada-multilib -l pl.UTF-8
Ten pakiet dodaje eksperymentalne wsparcie dla kompilacji programów w
Adzie.

%package -n libgnat
Summary:	Ada standard libraries
Summary(es.UTF-8):	Bibliotecas estándares de Ada
Summary(pl.UTF-8):	Biblioteki standardowe dla Ady
License:	GPL v2+ with linking exception
Group:		Libraries
Obsoletes:	gnat
Obsoletes:	libgnat1

%description -n libgnat
This package contains shared libraries needed to run programs written
in Ada.

%description -n libgnat -l es.UTF-8
Este paquete contiene las bibliotecas compartidas necesarias para
ejecutar programas escritos en Ada.

%description -n libgnat -l pl.UTF-8
Ten pakiet zawiera biblioteki potrzebne do uruchamiania programów
napisanych w Adzie.

%package -n libgnat-multilib
Summary:	Ada standard libraries
Summary(es.UTF-8):	Bibliotecas estándares de Ada
Summary(pl.UTF-8):	Biblioteki standardowe dla Ady
License:	GPL v2+ with linking exception
Group:		Libraries

%description -n libgnat-multilib
This package contains shared libraries needed to run programs written
in Ada.

%description -n libgnat-multilib -l es.UTF-8
Este paquete contiene las bibliotecas compartidas necesarias para
ejecutar programas escritos en Ada.

%description -n libgnat-multilib -l pl.UTF-8
Ten pakiet zawiera biblioteki potrzebne do uruchamiania programów
napisanych w Adzie.

%package -n libgnat-static
Summary:	Static Ada standard libraries
Summary(pl.UTF-8):	Statyczne biblioteki standardowe dla Ady
License:	GPL v2+ with linking exception
Group:		Development/Libraries
Obsoletes:	gnat-static

%description -n libgnat-static
This package contains static libraries for programs written in Ada.

%description -n libgnat-static -l pl.UTF-8
Ten pakiet zawiera biblioteki statyczne dla programów napisanych w
Adzie.

%package -n libgnat-multilib-static
Summary:	Static Ada standard libraries
Summary(pl.UTF-8):	Statyczne biblioteki standardowe dla Ady
License:	GPL v2+ with linking exception
Group:		Development/Libraries

%description -n libgnat-multilib-static
This package contains static libraries for programs written in Ada.

%description -n libgnat-multilib-static -l pl.UTF-8
Ten pakiet zawiera biblioteki statyczne dla programów napisanych w
Adzie.

%package c++
Summary:	C++ support for gcc
Summary(es.UTF-8):	Soporte de C++ para gcc
Summary(pl.UTF-8):	Obsługa C++ dla gcc
Summary(pt_BR.UTF-8):	Suporte C++ para o gcc
Group:		Development/Languages
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	egcc-c++
Obsoletes:	egcs-c++
Obsoletes:	gcc4-c++

%description c++
This package adds C++ support to the GNU Compiler Collection. It
includes support for most of the current C++ specification, including
templates and exception handling. It does not include a standard C++
library, which is available separately.

%description c++ -l de.UTF-8
Dieses Paket enthält die C++-Unterstützung für den
GNU-Compiler-Collection. Es unterstützt die aktuelle
C++-Spezifikation, inkl. Templates und Ausnahmeverarbeitung. Eine
C++-Standard-Library ist nicht enthalten - sie ist getrennt
erhältlich.

%description c++ -l es.UTF-8
Este paquete añade soporte de C++ al GCC (colección de compiladores
GNU). Ello incluye el soporte para la mayoría de la especificación
actual de C++, incluyendo plantillas y manejo de excepciones. No
incluye la biblioteca estándar de C++, la que es disponible separada.

%description c++ -l fr.UTF-8
Ce package ajoute un support C++ a la collection de compilateurs GNU.
Il comprend un support pour la plupart des spécifications actuelles de
C++, dont les modéles et la gestion des exceptions. Il ne comprend pas
une bibliothéque C++ standard, qui est disponible séparément.

%description c++ -l pl.UTF-8
Ten pakiet dodaje obsługę C++ do kompilatora gcc. Ma wsparcie dla
dużej ilości obecnych specyfikacji C++, nie zawiera natomiast
standardowych bibliotek C++, które są w oddzielnym pakiecie.

%description c++ -l pt_BR.UTF-8
Este pacote adiciona suporte C++ para o gcc.

%description c++ -l tr.UTF-8
Bu paket, GNU C derleyicisine C++ desteği ekler. 'Template'ler ve
aykırı durum işleme gibi çoğu güncel C++ tanımlarına uyar. Standart
C++ kitaplığı bu pakette yer almaz.

%package c++-multilib
Summary:	C++ support for gcc
Summary(es.UTF-8):	Soporte de C++ para gcc
Summary(pl.UTF-8):	Obsługa C++ dla gcc
Summary(pt_BR.UTF-8):	Suporte C++ para o gcc
Group:		Development/Languages
Requires:	%{name}-c++
Requires:	%{name}-multilib

%description c++-multilib
This package adds C++ support to the GNU Compiler Collection. It
includes support for most of the current C++ specification, including
templates and exception handling. It does not include a standard C++
library, which is available separately.

%description c++-multilib -l de.UTF-8
Dieses Paket enthält die C++-Unterstützung für den
GNU-Compiler-Collection. Es unterstützt die aktuelle
C++-Spezifikation, inkl. Templates und Ausnahmeverarbeitung. Eine
C++-Standard-Library ist nicht enthalten - sie ist getrennt
erhältlich.

%description c++-multilib -l es.UTF-8
Este paquete añade soporte de C++ al GCC (colección de compiladores
GNU). Ello incluye el soporte para la mayoría de la especificación
actual de C++, incluyendo plantillas y manejo de excepciones. No
incluye la biblioteca estándar de C++, la que es disponible separada.

%description c++-multilib -l fr.UTF-8
Ce package ajoute un support C++ a la collection de compilateurs GNU.
Il comprend un support pour la plupart des spécifications actuelles de
C++, dont les modéles et la gestion des exceptions. Il ne comprend pas
une bibliothéque C++ standard, qui est disponible séparément.

%description c++-multilib -l pl.UTF-8
Ten pakiet dodaje obsługę C++ do kompilatora gcc. Ma wsparcie dla
dużej ilości obecnych specyfikacji C++, nie zawiera natomiast
standardowych bibliotek C++, które są w oddzielnym pakiecie.

%description c++-multilib -l pt_BR.UTF-8
Este pacote adiciona suporte C++ para o gcc.

%description c++-multilib -l tr.UTF-8
Bu paket, GNU C derleyicisine C++ desteği ekler. 'Template'ler ve
aykırı durum işleme gibi çoğu güncel C++ tanımlarına uyar. Standart
C++ kitaplığı bu pakette yer almaz.

%package -n libstdc++
Summary:	GNU C++ library
Summary(es.UTF-8):	Biblioteca C++ de GNU
Summary(pl.UTF-8):	Biblioteki GNU C++
Summary(pt_BR.UTF-8):	Biblioteca C++ GNU
License:	GPL v2+ with free software exception
Group:		Libraries
# >= instead of = to allow keeping older libstdc++ (with different soname)
Requires:	libgcc >= %{epoch}:%{version}-%{release}
Obsoletes:	libg++
Obsoletes:	libstdc++3
Obsoletes:	libstdc++4

%description -n libstdc++
This is the GNU implementation of the standard C++ libraries, along
with additional GNU tools. This package includes the shared libraries
necessary to run C++ applications.

%description -n libstdc++ -l de.UTF-8
Dies ist die GNU-Implementierung der Standard-C++-Libraries mit
weiteren GNU-Tools. Dieses Paket enthält die zum Ausführen von
C++-Anwendungen erforderlichen gemeinsam genutzten Libraries.

%description -n libstdc++ -l es.UTF-8
Este es el soporte de las bibliotecas padrón del C++, junto con
herramientas GNU adicionales. El paquete incluye las bibliotecas
compartidas necesarias para ejecutar aplicaciones C++.

%description -n libstdc++ -l fr.UTF-8
Ceci est l'implémentation GNU des librairies C++ standard, ainsi que
des outils GNU supplémentaires. Ce package comprend les librairies
partagées nécessaires à l'exécution d'application C++.

%description -n libstdc++ -l pl.UTF-8
Pakiet ten zawiera biblioteki będące implementacją standardowych
bibliotek C++. Znajdują się w nim biblioteki dynamiczne niezbędne do
uruchomienia aplikacji napisanych w C++.

%description -n libstdc++ -l pt_BR.UTF-8
Este pacote é uma implementação da biblioteca padrão C++ v3, um
subconjunto do padrão ISO 14882.

%description -n libstdc++ -l tr.UTF-8
Bu paket, standart C++ kitaplıklarının GNU gerçeklemesidir ve C++
uygulamalarının koşturulması için gerekli kitaplıkları içerir.

%package -n libstdc++-multilib
Summary:	GNU C++ library
Summary(es.UTF-8):	Biblioteca C++ de GNU
Summary(pl.UTF-8):	Biblioteki GNU C++
Summary(pt_BR.UTF-8):	Biblioteca C++ GNU
License:	GPL v2+ with free software exception
Group:		Libraries
# >= instead of = to allow keeping older libstdc++ (with different soname)
Requires:	libgcc-multilib >= %{epoch}:%{version}-%{release}

%description -n libstdc++-multilib
This is the GNU implementation of the standard C++ libraries, along
with additional GNU tools. This package includes the shared libraries
necessary to run C++ applications.

%description -n libstdc++-multilib -l de.UTF-8
Dies ist die GNU-Implementierung der Standard-C++-Libraries mit
weiteren GNU-Tools. Dieses Paket enthält die zum Ausführen von
C++-Anwendungen erforderlichen gemeinsam genutzten Libraries.

%description -n libstdc++-multilib -l es.UTF-8
Este es el soporte de las bibliotecas padrón del C++, junto con
herramientas GNU adicionales. El paquete incluye las bibliotecas
compartidas necesarias para ejecutar aplicaciones C++.

%description -n libstdc++-multilib -l fr.UTF-8
Ceci est l'implémentation GNU des librairies C++ standard, ainsi que
des outils GNU supplémentaires. Ce package comprend les librairies
partagées nécessaires à l'exécution d'application C++.

%description -n libstdc++-multilib -l pl.UTF-8
Pakiet ten zawiera biblioteki będące implementacją standardowych
bibliotek C++. Znajdują się w nim biblioteki dynamiczne niezbędne do
uruchomienia aplikacji napisanych w C++.

%description -n libstdc++-multilib -l pt_BR.UTF-8
Este pacote é uma implementação da biblioteca padrão C++ v3, um
subconjunto do padrão ISO 14882.

%description -n libstdc++-multilib -l tr.UTF-8
Bu paket, standart C++ kitaplıklarının GNU gerçeklemesidir ve C++
uygulamalarının koşturulması için gerekli kitaplıkları içerir.

%package -n libstdc++-devel
Summary:	Header files and documentation for C++ development
Summary(de.UTF-8):	Header-Dateien zur Entwicklung mit C++
Summary(es.UTF-8):	Ficheros de cabecera y documentación para desarrollo C++
Summary(fr.UTF-8):	Fichiers d'en-tête et biblitothèques pour développer en C++
Summary(pl.UTF-8):	Pliki nagłówkowe i dokumentacja do biblioteki standardowej C++
Summary(pt_BR.UTF-8):	Arquivos de inclusão e bibliotecas para o desenvolvimento em C++
Summary(tr.UTF-8):	C++ ile program geliştirmek için gerekli dosyalar
License:	GPL v2+ with free software exception
Group:		Development/Libraries
Requires:	%{name}-c++ = %{epoch}:%{version}-%{release}
Requires:	glibc-devel
Requires:	libstdc++ = %{epoch}:%{version}-%{release}
Obsoletes:	libg++-devel
Obsoletes:	libstdc++3-devel
Obsoletes:	libstdc++4-devel

%description -n libstdc++-devel
This is the GNU implementation of the standard C++ libraries. This
package includes the header files needed for C++ development and
library documentation.

%description -n libstdc++-devel -l es.UTF-8
Este es el soporte de las bibliotecas padrón del lenguaje C++. Este
paquete incluye los archivos de inclusión y bibliotecas necesarios
para desarrollo de programas en lenguaje C++.

%description -n libstdc++-devel -l pl.UTF-8
Pakiet ten zawiera biblioteki będące implementacją standardowych
bibliotek C++. Znajdują się w nim pliki nagłówkowe wykorzystywane przy
programowaniu w języku C++ oraz dokumentacja biblioteki standardowej.

%description -n libstdc++-devel -l pt_BR.UTF-8
Este pacote inclui os arquivos de inclusão e bibliotecas necessárias
para desenvolvimento de programas C++.

%package -n libstdc++-multilib-devel
Summary:	Header files and documentation for C++ development
Summary(de.UTF-8):	Header-Dateien zur Entwicklung mit C++
Summary(es.UTF-8):	Ficheros de cabecera y documentación para desarrollo C++
Summary(fr.UTF-8):	Fichiers d'en-tête et biblitothèques pour développer en C++
Summary(pl.UTF-8):	Pliki nagłówkowe i dokumentacja do biblioteki standardowej C++
Summary(pt_BR.UTF-8):	Arquivos de inclusão e bibliotecas para o desenvolvimento em C++
Summary(tr.UTF-8):	C++ ile program geliştirmek için gerekli dosyalar
License:	GPL v2+ with free software exception
Group:		Development/Libraries
Requires:	%{name}-c++-multilib
Requires:	libstdc++-devel = %{epoch}:%{version}-%{release}
Requires:	libstdc++-multilib = %{epoch}:%{version}-%{release}

%description -n libstdc++-multilib-devel
This is the GNU implementation of the standard C++ libraries. This
package includes the header files needed for C++ development and
library documentation.

%description -n libstdc++-multilib-devel -l es.UTF-8
Este es el soporte de las bibliotecas padrón del lenguaje C++. Este
paquete incluye los archivos de inclusión y bibliotecas necesarios
para desarrollo de programas en lenguaje C++.

%description -n libstdc++-multilib-devel -l pl.UTF-8
Pakiet ten zawiera biblioteki będące implementacją standardowych
bibliotek C++. Znajdują się w nim pliki nagłówkowe wykorzystywane przy
programowaniu w języku C++ oraz dokumentacja biblioteki standardowej.

%description -n libstdc++-multilib-devel -l pt_BR.UTF-8
Este pacote inclui os arquivos de inclusão e bibliotecas necessárias
para desenvolvimento de programas C++.

%package -n libstdc++-static
Summary:	Static C++ standard library
Summary(es.UTF-8):	Biblioteca estándar estática de C++
Summary(pl.UTF-8):	Statyczna biblioteka standardowa C++
License:	GPL v2+ with free software exception
Group:		Development/Libraries
Requires:	libstdc++-devel = %{epoch}:%{version}-%{release}
Obsoletes:	libstdc++4-static

%description -n libstdc++-static
Static C++ standard library.

%description -n libstdc++-static -l es.UTF-8
Biblioteca estándar estática de C++.

%description -n libstdc++-static -l pl.UTF-8
Statyczna biblioteka standardowa C++.

%package -n libstdc++-multilib-static
Summary:	Static C++ standard library
Summary(es.UTF-8):	Biblioteca estándar estática de C++
Summary(pl.UTF-8):	Statyczna biblioteka standardowa C++
License:	GPL v2+ with free software exception
Group:		Development/Libraries
Requires:	libstdc++-multilib-devel

%description -n libstdc++-multilib-static
Static C++ standard library.

%description -n libstdc++-multilib-static -l es.UTF-8
Biblioteca estándar estática de C++.

%description -n libstdc++-multilib-static -l pl.UTF-8
Statyczna biblioteka standardowa C++.

%package fortran
Summary:	Fortran 95 support for gcc
Summary(es.UTF-8):	Soporte de Fortran 95 para gcc
Summary(pl.UTF-8):	Obsługa Fortranu 95 dla gcc
Summary(pt_BR.UTF-8):	Suporte Fortran 95 para o GCC
Group:		Development/Languages/Fortran
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	libgfortran = %{epoch}:%{version}-%{release}
Provides:	gcc-g77 = %{epoch}:%{version}-%{release}
Obsoletes:	egcs-g77
Obsoletes:	gcc-g77

%description fortran
This package adds support for compiling Fortran 95 programs with the
GNU compiler.

%description fortran -l es.UTF-8
Este paquete añade soporte para compilar programas escritos en Fortran
95 con el compilador GNU.

%description fortran -l pl.UTF-8
Ten pakiet dodaje obsługę Fortranu 95 do kompilatora gcc. Jest
potrzebny do kompilowania programów pisanych w języku Fortran 95.

%description fortran -l pt_BR.UTF-8
Suporte Fortran 95 para o GCC.

%package fortran-multilib
Summary:	Fortran 95 support for gcc
Summary(es.UTF-8):	Soporte de Fortran 95 para gcc
Summary(pl.UTF-8):	Obsługa Fortranu 95 dla gcc
Summary(pt_BR.UTF-8):	Suporte Fortran 95 para o GCC
Group:		Development/Languages/Fortran
Requires:	%{name}-fortran
Requires:	libgfortran-multilib

%description fortran-multilib
This package adds support for compiling Fortran 95 programs with the
GNU compiler.

%description fortran-multilib -l es.UTF-8
Este paquete añade soporte para compilar programas escritos en Fortran
95 con el compilador GNU.

%description fortran-multilib -l pl.UTF-8
Ten pakiet dodaje obsługę Fortranu 95 do kompilatora gcc. Jest
potrzebny do kompilowania programów pisanych w języku Fortran 95.

%description fortran-multilib -l pt_BR.UTF-8
Suporte Fortran 95 para o GCC.

%package -n libgfortran
Summary:	Fortran 95 Libraries
Summary(es.UTF-8):	Bibliotecas de Fortran 95
Summary(pl.UTF-8):	Biblioteki Fortranu 95
License:	GPL v2+ with unlimited link permission
Group:		Libraries
Obsoletes:	libg2c

%description -n libgfortran
Fortran 95 Libraries.

%description -n libgfortran -l es.UTF-8
Bibliotecas de Fortran 95.

%description -n libgfortran -l pl.UTF-8
Biblioteki Fortranu 95.

%package -n libgfortran-multilib
Summary:	Fortran 95 Libraries
Summary(es.UTF-8):	Bibliotecas de Fortran 95
Summary(pl.UTF-8):	Biblioteki Fortranu 95
License:	GPL v2+ with unlimited link permission
Group:		Libraries

%description -n libgfortran-multilib
Fortran 95 Libraries.

%description -n libgfortran-multilib -l es.UTF-8
Bibliotecas de Fortran 95.

%description -n libgfortran-multilib -l pl.UTF-8
Biblioteki Fortranu 95.

%package -n libgfortran-static
Summary:	Static Fortran 95 Libraries
Summary(es.UTF-8):	Bibliotecas estáticas de Fortran 95
Summary(pl.UTF-8):	Statyczne Biblioteki Fortranu 95
License:	GPL v2+ with unlimited link permission
Group:		Development/Libraries
Requires:	libgfortran = %{epoch}:%{version}-%{release}
Obsoletes:	libg2c-static

%description -n libgfortran-static
Static Fortran 95 Libraries.

%description -n libgfortran-static -l es.UTF-8
Bibliotecas estáticas de Fortran 95.

%description -n libgfortran-static -l pl.UTF-8
Statyczne biblioteki Fortranu 95.

%package -n libgfortran-multilib-static
Summary:	Static Fortran 95 Libraries
Summary(es.UTF-8):	Bibliotecas estáticas de Fortran 95
Summary(pl.UTF-8):	Statyczne Biblioteki Fortranu 95
License:	GPL v2+ with unlimited link permission
Group:		Development/Libraries
Requires:	libgfortran-multilib

%description -n libgfortran-multilib-static
Static Fortran 95 Libraries.

%description -n libgfortran-multilib-static -l es.UTF-8
Bibliotecas estáticas de Fortran 95.

%description -n libgfortran-multilib-static -l pl.UTF-8
Statyczne biblioteki Fortranu 95.

%package java
Summary:	Java support for gcc
Summary(es.UTF-8):	Soporte de Java para gcc
Summary(pl.UTF-8):	Obsługa Javy dla gcc
Group:		Development/Languages/Java
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	libgcj-devel = %{epoch}:%{version}-%{release}
Provides:	gcc-java-tools
Provides:	gcj = %{epoch}:%{version}-%{release}
Obsoletes:	eclipse-ecj
Obsoletes:	gcc-java-tools
Obsoletes:	java-gnu-classpath-tools

%description java
This package adds experimental support for compiling Java(TM) programs
and bytecode into native code. To use this you will also need the
libgcj package.

%description java -l es.UTF-8
Este paquete añade soporte experimental para compilar programas
Java(tm) y su bytecode en código nativo. Para usarlo también va a
necesitar el paquete libgcj.

%description java -l pl.UTF-8
Ten pakiet dodaje możliwość kompilowania programów w języku Java(TM)
oraz bajtkodu do kodu natywnego. Do używania go wymagany jest
dodatkowo pakiet libgcj.

%package -n libgcj
Summary:	Java Class Libraries
Summary(es.UTF-8):	Bibliotecas de clases de Java
Summary(pl.UTF-8):	Biblioteki Klas Javy
License:	GPL v2+ with limited linking exception
Group:		Libraries
Requires:	jpackage-utils
Provides:	java(ClassDataVersion) = %{_classdataversion}
Obsoletes:	libgcj3

%description -n libgcj
Java Class Libraries.

%description -n libgcj -l es.UTF-8
Bibliotecas de clases de Java.

%description -n libgcj -l pl.UTF-8
Biblioteki Klas Javy.

%package -n libgcj-devel
Summary:	Development files for Java Class Libraries
Summary(es.UTF-8):	Ficheros de desarrollo para las bibliotecas de clases de Java
Summary(pl.UTF-8):	Pliki nagłówkowe dla Bibliotek Klas Javy
License:	GPL v2+ with limited linking exception
Group:		Development/Libraries
Requires:	libgcj = %{epoch}:%{version}-%{release}
Requires:	zlib-devel
Obsoletes:	libgcj3-devel

%description -n libgcj-devel
Development files for Java Class Libraries.

%description -n libgcj-devel -l es.UTF-8
Ficheros de desarrollo para las bibliotecas de clases de Java.

%description -n libgcj-devel -l pl.UTF-8
Pliki nagłówkowe dla Bibliotek Klas Javy.

%package -n libgcj-static
Summary:	Static Java Class Libraries
Summary(es.UTF-8):	Bibliotecas estáticas de clases de Java
Summary(pl.UTF-8):	Statyczne Biblioteki Klas Javy
License:	GPL v2+ with limited linking exception
Group:		Development/Libraries
Requires:	libgcj-devel = %{epoch}:%{version}-%{release}
Requires:	libstdc++-devel = %{epoch}:%{version}-%{release}

%description -n libgcj-static
Static Java Class Libraries.

%description -n libgcj-static -l es.UTF-8
Bibliotecas estáticas de clases de Java.

%description -n libgcj-static -l pl.UTF-8
Statyczne Biblioteki Klas Javy.

%package -n libffi
Summary:	Foreign Function Interface library
Summary(es.UTF-8):	Biblioteca de interfaz de funciones ajenas
Summary(pl.UTF-8):	Biblioteka zewnętrznych wywołań funkcji
License:	BSD-like
Group:		Libraries

%description -n libffi
The libffi library provides a portable, high level programming
interface to various calling conventions. This allows a programmer to
call any function specified by a call interface description at run
time.

%description -n libffi -l es.UTF-8
La biblioteca libffi provee una interfaz portable de programación de
alto nivel para varias convenciones de llamada. Ello permite que un
programador llame una función cualquiera especificada por una
descripción de interfaz de llamada en el tiempo de ejecución.

%description -n libffi -l pl.UTF-8
Biblioteka libffi dostarcza przenośnego, wysokopoziomowego
międzymordzia do różnych konwencji wywołań funkcji. Pozwala to
programiście wywoływać dowolne funkcje podając konwencję wywołania w
czasie wykonania.

%package -n libffi-multilib
Summary:	Foreign Function Interface library
Summary(es.UTF-8):	Biblioteca de interfaz de funciones ajenas
Summary(pl.UTF-8):	Biblioteka zewnętrznych wywołań funkcji
License:	BSD-like
Group:		Libraries

%description -n libffi-multilib
The libffi library provides a portable, high level programming
interface to various calling conventions. This allows a programmer to
call any function specified by a call interface description at run
time.

%description -n libffi-multilib -l es.UTF-8
La biblioteca libffi provee una interfaz portable de programación de
alto nivel para varias convenciones de llamada. Ello permite que un
programador llame una función cualquiera especificada por una
descripción de interfaz de llamada en el tiempo de ejecución.

%description -n libffi-multilib -l pl.UTF-8
Biblioteka libffi dostarcza przenośnego, wysokopoziomowego
międzymordzia do różnych konwencji wywołań funkcji. Pozwala to
programiście wywoływać dowolne funkcje podając konwencję wywołania w
czasie wykonania.

%package -n libffi-devel
Summary:	Development files for Foreign Function Interface library
Summary(es.UTF-8):	Ficheros de desarrollo para libffi
Summary(pl.UTF-8):	Pliki nagłówkowe dla libffi
License:	BSD-like
Group:		Development/Libraries
Requires:	libffi = %{epoch}:%{version}-%{release}

%description -n libffi-devel
Development files for Foreign Function Interface library.

%description -n libffi-devel -l es.UTF-8
Ficheros de desarrollo para libffi.

%description -n libffi-devel -l pl.UTF-8
Pliki nagłówkowe dla libffi.

%package -n libffi-multilib-devel
Summary:	Development files for Foreign Function Interface library
Summary(es.UTF-8):	Ficheros de desarrollo para libffi
Summary(pl.UTF-8):	Pliki nagłówkowe dla libffi
License:	BSD-like
Group:		Development/Libraries
Requires:	libffi-devel
Requires:	libffi-multilib

%description -n libffi-multilib-devel
Development files for Foreign Function Interface library.

%description -n libffi-multilib-devel -l es.UTF-8
Ficheros de desarrollo para libffi.

%description -n libffi-multilib-devel -l pl.UTF-8
Pliki nagłówkowe dla libffi.

%package -n libffi-static
Summary:	Static Foreign Function Interface library
Summary(es.UTF-8):	Biblioteca libffi estática
Summary(pl.UTF-8):	Statyczna biblioteka libffi
License:	BSD-like
Group:		Development/Libraries
Requires:	libffi-devel = %{epoch}:%{version}-%{release}

%description -n libffi-static
Static Foreign Function Interface library.

%description -n libffi-static -l es.UTF-8
Biblioteca libffi estática.

%description -n libffi-static -l pl.UTF-8
Statyczna biblioteka libffi.

%package -n libffi-multilib-static
Summary:	Static Foreign Function Interface library
Summary(es.UTF-8):	Biblioteca libffi estática
Summary(pl.UTF-8):	Statyczna biblioteka libffi
License:	BSD-like
Group:		Development/Libraries
Requires:	libffi-multilib-devel

%description -n libffi-multilib-static
Static Foreign Function Interface library.

%description -n libffi-multilib-static -l es.UTF-8
Biblioteca libffi estática.

%description -n libffi-multilib-static -l pl.UTF-8
Statyczna biblioteka libffi.

%package objc
Summary:	Objective C support for gcc
Summary(de.UTF-8):	Objektive C-Unterstützung für gcc
Summary(es.UTF-8):	Soporte de Objective C para gcc
Summary(fr.UTF-8):	Gestion d'Objective C pour gcc
Summary(pl.UTF-8):	Obsługa obiektowego C dla kompilatora gcc
Summary(tr.UTF-8):	gcc için Objective C desteği
Group:		Development/Languages
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	libobjc = %{epoch}:%{version}-%{release}
Obsoletes:	egcc-objc
Obsoletes:	egcs-objc

%description objc
This package adds Objective C support to the GNU Compiler Collection.
Objective C is a object oriented derivative of the C language, mainly
used on systems running NeXTSTEP. This package does not include the
standard objective C object library.

%description objc -l de.UTF-8
Dieses Paket ergänzt den GNU-Compiler-Collection durch
Objective-C-Support. Objective C ist ein objektorientiertes Derivat
von C, das zur Hauptsache auf Systemen mit NeXTSTEP zum Einsatz kommt.
Die Standard-Objective-C-Objekt-Library ist nicht Teil des Pakets.

%description objc -l es.UTF-8
Este paquete añade soporte de Objective C al GCC (colección de
compiladores GNU). Objective C es un lenguaje orientado a objetos
derivado de C, principalmente usado en sistemas que funcionan bajo
NeXTSTEP. El paquete no incluye la biblioteca de objetos estándar de
Objective C.

%description objc -l fr.UTF-8
Ce package ajoute un support Objective C a la collection de
compilateurs GNU. L'Objective C est un langage orienté objetdérivé du
langage C, principalement utilisé sur les systèmes NeXTSTEP. Ce
package n'inclue pas la bibliothéque Objective C standard.

%description objc -l pl.UTF-8
Ten pakiet dodaje obsługę obiektowego C do kompilatora gcc. Obiektowe
C (objc) jest zorientowaną obiektowo pochodną języka C, używaną
głównie w systemach używających NeXTSTEP. W pakiecie nie ma
standardowej biblioteki objc (która znajduje się w osobnym pakiecie).

%description objc -l tr.UTF-8
Bu paket, GNU C derleyicisine Objective C desteği ekler. Objective C,
C dilinin nesne yönelik bir türevidir ve NeXTSTEP altında çalışan
sistemlerde yaygın olarak kullanılır. Standart Objective C nesne
kitaplığı bu pakette yer almaz.

%package objc-multilib
Summary:	Objective C support for gcc
Summary(de.UTF-8):	Objektive C-Unterstützung für gcc
Summary(es.UTF-8):	Soporte de Objective C para gcc
Summary(fr.UTF-8):	Gestion d'Objective C pour gcc
Summary(pl.UTF-8):	Obsługa obiektowego C dla kompilatora gcc
Summary(tr.UTF-8):	gcc için Objective C desteği
Group:		Development/Languages
Requires:	%{name}-multilib
Requires:	libobjc-multilib

%description objc-multilib
This package adds Objective C support to the GNU Compiler Collection.
Objective C is a object oriented derivative of the C language, mainly
used on systems running NeXTSTEP. This package does not include the
standard objective C object library.

%description objc-multilib -l de.UTF-8
Dieses Paket ergänzt den GNU-Compiler-Collection durch
Objective-C-Support. Objective C ist ein objektorientiertes Derivat
von C, das zur Hauptsache auf Systemen mit NeXTSTEP zum Einsatz kommt.
Die Standard-Objective-C-Objekt-Library ist nicht Teil des Pakets.

%description objc-multilib -l es.UTF-8
Este paquete añade soporte de Objective C al GCC (colección de
compiladores GNU). Objective C es un lenguaje orientado a objetos
derivado de C, principalmente usado en sistemas que funcionan bajo
NeXTSTEP. El paquete no incluye la biblioteca de objetos estándar de
Objective C.

%description objc-multilib -l fr.UTF-8
Ce package ajoute un support Objective C a la collection de
compilateurs GNU. L'Objective C est un langage orienté objetdérivé du
langage C, principalement utilisé sur les systèmes NeXTSTEP. Ce
package n'inclue pas la bibliothéque Objective C standard.

%description objc-multilib -l pl.UTF-8
Ten pakiet dodaje obsługę obiektowego C do kompilatora gcc. Obiektowe
C (objc) jest zorientowaną obiektowo pochodną języka C, używaną
głównie w systemach używających NeXTSTEP. W pakiecie nie ma
standardowej biblioteki objc (która znajduje się w osobnym pakiecie).

%description objc-multilib -l tr.UTF-8
Bu paket, GNU C derleyicisine Objective C desteği ekler. Objective C,
C dilinin nesne yönelik bir türevidir ve NeXTSTEP altında çalışan
sistemlerde yaygın olarak kullanılır. Standart Objective C nesne
kitaplığı bu pakette yer almaz.

%package objc++
Summary:	Objective C++ support for gcc
Summary(pl.UTF-8):	Obsługa języka Objective C++ dla gcc
Group:		Development/Languages
Requires:	%{name}-c++ = %{epoch}:%{version}-%{release}
Requires:	%{name}-objc = %{epoch}:%{version}-%{release}

%description objc++
This package adds Objective C++ support to the GNU Compiler
Collection.

%description objc++ -l pl.UTF-8
Ten pakiet dodaje obsługę języka Objective C++ do zestawu kompilatorów
GNU Compiler Collection.

%package -n libobjc
Summary:	Objective C Libraries
Summary(es.UTF-8):	Bibliotecas de Objective C
Summary(pl.UTF-8):	Biblioteki Obiektowego C
License:	GPL v2+ with linking exception
Group:		Libraries
Obsoletes:	libobjc1

%description -n libobjc
Objective C Libraries.

%description -n libobjc -l es.UTF-8
Bibliotecas de Objective C.

%description -n libobjc -l pl.UTF-8
Biblioteki Obiektowego C.

%package -n libobjc-multilib
Summary:	Objective C Libraries
Summary(es.UTF-8):	Bibliotecas de Objective C
Summary(pl.UTF-8):	Biblioteki Obiektowego C
License:	GPL v2+ with linking exception
Group:		Libraries

%description -n libobjc-multilib
Objective C Libraries.

%description -n libobjc-multilib -l es.UTF-8
Bibliotecas de Objective C.

%description -n libobjc-multilib -l pl.UTF-8
Biblioteki Obiektowego C.

%package -n libobjc-static
Summary:	Static Objective C Libraries
Summary(es.UTF-8):	Bibliotecas estáticas de Objective C
Summary(pl.UTF-8):	Statyczne Biblioteki Obiektowego C
License:	GPL v2+ with linking exception
Group:		Development/Libraries
Requires:	libobjc = %{epoch}:%{version}-%{release}

%description -n libobjc-static
Static Objective C Libraries.

%description -n libobjc-static -l es.UTF-8
Bibliotecas estáticas de Objective C.

%description -n libobjc-static -l pl.UTF-8
Statyczne biblioteki Obiektowego C.

%package -n libobjc-multilib-static
Summary:	Static Objective C Libraries
Summary(es.UTF-8):	Bibliotecas estáticas de Objective C
Summary(pl.UTF-8):	Statyczne Biblioteki Obiektowego C
License:	GPL v2+ with linking exception
Group:		Development/Libraries
Requires:	libobjc-multilib

%description -n libobjc-multilib-static
Static Objective C Libraries.

%description -n libobjc-multilib-static -l es.UTF-8
Bibliotecas estáticas de Objective C.

%description -n libobjc-multilib-static -l pl.UTF-8
Statyczne biblioteki Obiektowego C.

%prep
%setup -q
%patch100 -p0
%patch101 -p0
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p0
%if %{with qt}
%patch8 -p1
%endif
%patch9 -p1
%patch10 -p0
%patch11 -p0

mv ChangeLog ChangeLog.general

%if %{with java}
# see contrib/download_ecj
install %{SOURCE2} ecj.jar
%endif

# override snapshot version.
echo %{version} > gcc/BASE-VER
echo "release" > gcc/DEV-PHASE

%build
cd gcc
#{__autoconf}
cd ..
%if %{with qt}
cd libjava/classpath
%{__autoconf}
cd ../..
%endif
cp -f /usr/share/automake/config.sub .

rm -rf builddir && install -d builddir && cd builddir

# http://www.mailinglistarchive.com/java%40gcc.gnu.org/msg02751.html
export JAR=no

CC="%{__cc}" \
CFLAGS="%{rpmcflags}" \
CXXFLAGS="%{rpmcxxflags}" \
TEXCONFIG=false \
../configure \
	--prefix=%{_prefix} \
	--with-local-prefix=%{_prefix}/local \
	--libdir=%{_libdir} \
	--libexecdir=%{_libdir} \
	--infodir=%{_infodir} \
	--mandir=%{_mandir} \
	--x-libraries=%{_libdir} \
	--enable-shared \
	--enable-threads=posix \
	--enable-linux-futex \
	--enable-languages="c%{?with_cxx:,c++}%{?with_fortran:,fortran}%{?with_objc:,objc}%{?with_objcxx:,obj-c++}%{?with_ada:,ada}%{?with_java:,java}" \
	--%{?with_gomp:en}%{!?with_gomp:dis}able-libgomp \
	--%{?with_mudflap:en}%{!?with_mudflap:dis}able-libmudflap \
	--enable-c99 \
	--enable-long-long \
	--enable-decimal-float=yes \
	--%{?with_multilib:en}%{!?with_multilib:dis}able-multilib \
	--enable-nls \
	--disable-werror \
%ifarch %{ix86} %{x8664}
	--disable-cld \
%endif
%ifarch sparc64
	--with-cpu=ultrasparc \
%endif
	--with-gnu-as \
	--with-gnu-ld \
	--with-demangler-in-ld \
	--with-system-zlib \
	--with-slibdir=%{_slibdir} \
%ifnarch ia64
	--without-system-libunwind \
%else
	--with-system-libunwind \
%endif
	%{!?with_java:--without-x} \
	%{?with_fortran:--enable-cmath} \
	--with-long-double-128 \
%ifarch ppc ppc64
	--enable-secureplt \
%endif
%if %{with cxx}
	--with-gxx-include-dir=%{_includedir}/c++/%{version} \
	--disable-libstdcxx-pch \
	--enable-__cxa_atexit \
	--enable-libstdcxx-allocator=new \
%endif
%if %{with java}
	--enable-libjava-multilib=no \
	%{!?with_alsa:--disable-alsa} \
	%{!?with_dssi:--disable-dssi} \
	--disable-gconf-peer \
%if %{with x}
	--enable-java-awt="xlib%{?with_gtk:,gtk}%{?with_qt:,qt}" \
%endif
	%{?with_mozilla:--enable-plugin} \
	--enable-libgcj \
	--enable-libgcj-multifile \
	--enable-libgcj-database \
	%{?with_gtk:--enable-gtk-cairo} \
	--enable-jni \
	--enable-xmlj \
%endif
	--%{?with_bootstrap:en}%{!?with_bootstrap:dis}able-bootstrap \
	--with-pkgversion="PLD-Linux" \
	--with-bugurl="http://bugs.pld-linux.org" \
	%{_target_platform}

cd ..

%{__make} -C builddir \
	%{?with_bootstrap:%{?with_profiling:profiledbootstrap}} \
	GCJFLAGS="%{rpmcflags}" \
	BOOT_CFLAGS="%{rpmcflags}" \
	STAGE1_CFLAGS="%{rpmcflags} -O0 -g0" \
	GNATLIBCFLAGS="%{rpmcflags}" \
	LDFLAGS_FOR_TARGET="%{rpmldflags}" \
	mandir=%{_mandir} \
	infodir=%{_infodir}

%if %{with tests}
if [ ! -r /dev/pts/0 ]; then
	echo "You need to have /dev/pts mounted to avoid expect's spawn failures!"
	exit 1
fi
%{__make} -k -C builddir check 2>&1 ||:
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/lib,%{_aclocaldir},%{_datadir},%{_infodir}}

cd builddir

%{__make} -j1 install \
	mandir=%{_mandir} \
	infodir=%{_infodir} \
	DESTDIR=$RPM_BUILD_ROOT

install gcc/specs $RPM_BUILD_ROOT%{_libdir}/gcc/%{_target_platform}/%{version}

%if %{with multilib}
# create links
%ifarch sparc64
ln -f $RPM_BUILD_ROOT%{_bindir}/sparc64-pld-linux-gcc \
	$RPM_BUILD_ROOT%{_bindir}/sparc-pld-linux-gcc
ln -f $RPM_BUILD_ROOT%{_bindir}/sparc64-pld-linux-gcc-%{version} \
	$RPM_BUILD_ROOT%{_bindir}/sparc-pld-linux-gcc-%{version}
%if %{with cxx}
ln -f $RPM_BUILD_ROOT%{_bindir}/sparc64-pld-linux-c++ \
	$RPM_BUILD_ROOT%{_bindir}/sparc-pld-linux-c++
ln -f $RPM_BUILD_ROOT%{_bindir}/sparc64-pld-linux-g++ \
	$RPM_BUILD_ROOT%{_bindir}/sparc-pld-linux-g++
%endif
%if %{with java}
ln -f $RPM_BUILD_ROOT%{_bindir}/sparc64-pld-linux-gcj \
	$RPM_BUILD_ROOT%{_bindir}/sparc-pld-linux-gcj
%endif
%endif
%endif

ln -sf %{_bindir}/cpp $RPM_BUILD_ROOT/lib/cpp
ln -sf gcc $RPM_BUILD_ROOT%{_bindir}/cc
echo ".so gcc.1" > $RPM_BUILD_ROOT%{_mandir}/man1/cc.1

libssp=$(cd $RPM_BUILD_ROOT%{_libdir}; echo libssp.so.*.*.*)
mv $RPM_BUILD_ROOT{%{_libdir}/$libssp,%{_slibdir}}
ln -sf %{_slibdir}/$libssp $RPM_BUILD_ROOT%{_libdir}/libssp.so
%if %{with multilib}
libssp=$(cd $RPM_BUILD_ROOT%{_libdir32}; echo libssp.so.*.*.*)
mv $RPM_BUILD_ROOT{%{_libdir32}/$libssp,%{_slibdir32}}
ln -sf %{_slibdir32}/$libssp $RPM_BUILD_ROOT%{_libdir32}/libssp.so
%endif

%if %{with fortran}
ln -sf gfortran $RPM_BUILD_ROOT%{_bindir}/g95
echo ".so gfortran.1" > $RPM_BUILD_ROOT%{_mandir}/man1/g95.1
%endif

%if %{with ada}
# move ada shared libraries to proper place...
mv -f	$RPM_BUILD_ROOT%{_libdir}/gcc/*/*/adalib/*.so.1 \
	$RPM_BUILD_ROOT%{_libdir}
# check if symlink to be made is valid
test -f	$RPM_BUILD_ROOT%{_libdir}/libgnat-4.4.so.1
ln -sf	libgnat-4.4.so.1 $RPM_BUILD_ROOT%{_libdir}/libgnat-4.4.so
ln -sf	libgnarl-4.4.so.1 $RPM_BUILD_ROOT%{_libdir}/libgnarl-4.4.so
ln -sf	libgnat-4.4.so $RPM_BUILD_ROOT%{_libdir}/libgnat.so
ln -sf	libgnarl-4.4.so $RPM_BUILD_ROOT%{_libdir}/libgnarl.so
%if %{with multilib}
mv -f	$RPM_BUILD_ROOT%{_libdir}/gcc/*/*/32/adalib/*.so.1 \
	$RPM_BUILD_ROOT%{_libdir32}
# check if symlink to be made is valid
test -f	$RPM_BUILD_ROOT%{_libdir32}/libgnat-4.4.so.1
ln -sf	libgnat-4.4.so.1 $RPM_BUILD_ROOT%{_libdir32}/libgnat-4.4.so
ln -sf	libgnarl-4.4.so.1 $RPM_BUILD_ROOT%{_libdir32}/libgnarl-4.4.so
ln -sf	libgnat-4.4.so $RPM_BUILD_ROOT%{_libdir32}/libgnat.so
ln -sf	libgnarl-4.4.so $RPM_BUILD_ROOT%{_libdir32}/libgnarl.so
%endif
%endif

cd ..

%if %{with java}
install -d java-doc
cp -f libjava/READ* java-doc
ln -sf libgcj-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/libgcj.jar
rm -f $RPM_BUILD_ROOT%{_libdir}/classpath/libgjs*.la
# tools.zip sources
rm -rf $RPM_BUILD_ROOT%{_datadir}/classpath/tools/gnu
%endif
%if %{with objc}
cp -f libobjc/README gcc/objc/README.libobjc
%endif

# gcj-$version-$gcjsonamever
%define	gcjdbexecdir	gcj-%{version}-10

# avoid -L poisoning in *.la - there should be only -L%{_libdir}/gcc/*/%{version}
# normalize libdir, to avoid propagation of unnecessary RPATHs by libtool
for f in libssp.la libssp_nonshared.la \
	%{?with_cxx:libstdc++.la libsupc++.la} \
	%{?with_fortran:libgfortran.la} \
	%{?with_gomp:libgomp.la} \
	%{?with_mudflap:libmudflap.la libmudflapth.la} \
%if %{with java}
	libffi.la libgcj.la libgcj-tools.la libgij.la \
	%{gcjdbexecdir}/libjvm.la \
	%{gcjdbexecdir}/libxmlj.la \
	%{?with_x:lib-gnu-awt-xlib.la} \
	%{?with_gtk:%{gcjdbexecdir}/libgtkpeer.la %{gcjdbexecdir}/libjawt.la} \
	%{?with_qt:%{gcjdbexecdir}/libqtpeer.la} \
	%{?with_alsa:%{gcjdbexecdir}/libgjsmalsa.la} \
	%{?with_dssi:%{gcjdbexecdir}/libgjsmdssi.la} \
%endif
	%{?with_objc:libobjc.la};
do
	%{__perl} %{SOURCE1} $RPM_BUILD_ROOT%{_libdir}/$f %{_libdir} > $RPM_BUILD_ROOT%{_libdir}/$f.fixed
	mv $RPM_BUILD_ROOT%{_libdir}/$f{.fixed,}
done
%if %{with multilib}
for f in libssp.la libssp_nonshared.la \
	%{?with_cxx:libstdc++.la libsupc++.la} \
	%{?with_fortran:libgfortran.la} \
	%{?with_gomp:libgomp.la} \
	%{?with_mudflap:libmudflap.la libmudflapth.la} \
	%{?with_java:libffi.la} \
	%{?with_objc:libobjc.la};
do
	%{__perl} %{SOURCE1} $RPM_BUILD_ROOT%{_libdir32}/$f %{_libdir32} > $RPM_BUILD_ROOT%{_libdir32}/$f.fixed
	mv $RPM_BUILD_ROOT%{_libdir32}/$f{.fixed,}
done
%endif

gccdir=$(echo $RPM_BUILD_ROOT%{_libdir}/gcc/*/*)
cp $gccdir/install-tools/include/*.h $gccdir/include
cp $gccdir/include-fixed/syslimits.h $gccdir/include
rm -rf $gccdir/install-tools
rm -rf $gccdir/include-fixed

%find_lang gcc
%find_lang cpplib
cat cpplib.lang >> gcc.lang

%if %{with cxx}
%find_lang libstdc\+\+
install libstdc++-v3/include/precompiled/* $RPM_BUILD_ROOT%{_includedir}
%endif

# svn snap doesn't contain (release does) below files,
# so let's create dummy entries to satisfy %%files.
[ ! -f NEWS ] && touch NEWS
[ ! -f libgfortran/AUTHORS ] && touch libgfortran/AUTHORS
[ ! -f libgfortran/README ] && touch libgfortran/README

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%post ada	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun ada	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%post fortran	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun fortran	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%post java	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun java	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%post	-p /sbin/ldconfig -n libgcc
%postun	-p /sbin/ldconfig -n libgcc
%post	-p /sbin/ldconfig -n libgcc-multilib
%postun	-p /sbin/ldconfig -n libgcc-multilib
%post	-p /sbin/ldconfig -n libgomp
%postun	-p /sbin/ldconfig -n libgomp
%post	-p /sbin/ldconfig -n libgomp-multilib
%postun	-p /sbin/ldconfig -n libgomp-multilib
%post	-p /sbin/ldconfig -n libmudflap
%postun	-p /sbin/ldconfig -n libmudflap
%post	-p /sbin/ldconfig -n libmudflap-multilib
%postun	-p /sbin/ldconfig -n libmudflap-multilib
%post	-p /sbin/ldconfig -n libgnat
%postun	-p /sbin/ldconfig -n libgnat
%post	-p /sbin/ldconfig -n libgnat-multilib
%postun	-p /sbin/ldconfig -n libgnat-multilib
%post	-p /sbin/ldconfig -n libstdc++
%postun	-p /sbin/ldconfig -n libstdc++
%post	-p /sbin/ldconfig -n libstdc++-multilib
%postun	-p /sbin/ldconfig -n libstdc++-multilib
%post	-p /sbin/ldconfig -n libgfortran
%postun	-p /sbin/ldconfig -n libgfortran
%post	-p /sbin/ldconfig -n libgfortran-multilib
%postun	-p /sbin/ldconfig -n libgfortran-multilib
%post	-p /sbin/ldconfig -n libgcj
%postun	-p /sbin/ldconfig -n libgcj
%post	-p /sbin/ldconfig -n libffi
%postun	-p /sbin/ldconfig -n libffi
%post	-p /sbin/ldconfig -n libffi-multilib
%postun	-p /sbin/ldconfig -n libffi-multilib
%post	-p /sbin/ldconfig -n libobjc
%postun	-p /sbin/ldconfig -n libobjc
%post	-p /sbin/ldconfig -n libobjc-multilib
%postun	-p /sbin/ldconfig -n libobjc-multilib

%files -f gcc.lang
%defattr(644,root,root,755)
%doc ChangeLog.general MAINTAINERS NEWS
# bugs.html faq.html
%doc gcc/{ChangeLog,ONEWS,README.Portability}
%dir %{_libdir}/gcc
%dir %{_libdir}/gcc/*
%dir %{_libdir}/gcc/*/*
%attr(755,root,root) %{_bindir}/*-gcc*
%attr(755,root,root) %{_bindir}/gcc
%attr(755,root,root) %{_bindir}/gccbug
%attr(755,root,root) %{_bindir}/gcov
%attr(755,root,root) %{_bindir}/cc
%attr(755,root,root) %{_bindir}/cpp
%{_mandir}/man1/cc.1*
%{_mandir}/man1/cpp.1*
%{_mandir}/man1/gcc.1*
%{_mandir}/man1/gcov.1*
%{_infodir}/cpp*
%{_infodir}/gcc*
%attr(755,root,root) /lib/cpp
%attr(755,root,root) %{_slibdir}/lib*.so
%{_libdir}/libssp.a
%{_libdir}/libssp.la
%attr(755,root,root) %{_libdir}/libssp.so
%{_libdir}/libssp_nonshared.a
%{_libdir}/libssp_nonshared.la
%{_libdir}/gcc/*/*/libgcov.a
%{_libdir}/gcc/*/*/libgcc.a
%{_libdir}/gcc/*/*/libgcc_eh.a
%{_libdir}/gcc/*/*/specs
%{_libdir}/gcc/*/*/crt*.o
%attr(755,root,root) %{_libdir}/gcc/*/*/cc1
%attr(755,root,root) %{_libdir}/gcc/*/*/collect2
%dir %{_libdir}/gcc/*/*/include
%dir %{_libdir}/gcc/*/*/include/ssp
%{_libdir}/gcc/*/*/include/ssp/*.h
%{_libdir}/gcc/*/*/include/float.h
%{_libdir}/gcc/*/*/include/iso646.h
%{_libdir}/gcc/*/*/include/limits.h
%{?with_gomp:%{_libdir}/gcc/*/*/include/omp.h}
%{_libdir}/gcc/*/*/include/stdarg.h
%{_libdir}/gcc/*/*/include/stdbool.h
%{_libdir}/gcc/*/*/include/stddef.h
%{_libdir}/gcc/*/*/include/stdfix.h
%{_libdir}/gcc/*/*/include/syslimits.h
%{_libdir}/gcc/*/*/include/unwind.h
%{_libdir}/gcc/*/*/include/varargs.h
%ifarch %{ix86} %{x8664}
%{_libdir}/gcc/*/*/include/ammintrin.h
%{_libdir}/gcc/*/*/include/avxintrin.h
%{_libdir}/gcc/*/*/include/bmmintrin.h
%{_libdir}/gcc/*/*/include/cpuid.h
%{_libdir}/gcc/*/*/include/cross-stdarg.h
%{_libdir}/gcc/*/*/include/emmintrin.h
%{_libdir}/gcc/*/*/include/immintrin.h
%{_libdir}/gcc/*/*/include/mm3dnow.h
%{_libdir}/gcc/*/*/include/mm_malloc.h
%{_libdir}/gcc/*/*/include/mmintrin-common.h
%{_libdir}/gcc/*/*/include/mmintrin.h
%{_libdir}/gcc/*/*/include/nmmintrin.h
%{_libdir}/gcc/*/*/include/pmmintrin.h
%{_libdir}/gcc/*/*/include/smmintrin.h
%{_libdir}/gcc/*/*/include/tmmintrin.h
%{_libdir}/gcc/*/*/include/wmmintrin.h
%{_libdir}/gcc/*/*/include/x86intrin.h
%{_libdir}/gcc/*/*/include/xmmintrin.h
%endif
%ifarch powerpc ppc ppc64
%{_libdir}/gcc/*/*/include/altivec.h
%{_libdir}/gcc/*/*/include/paired.h
%{_libdir}/gcc/*/*/include/ppc-asm.h
%{_libdir}/gcc/*/*/include/ppu_intrinsics.h
%{_libdir}/gcc/*/*/include/si2vmx.h
%{_libdir}/gcc/*/*/include/spe.h
%{_libdir}/gcc/*/*/include/spu2vmx.h
%{_libdir}/gcc/*/*/include/vec_types.h
%endif

%if %{with multilib}
%files multilib
%defattr(644,root,root,755)
%attr(755,root,root) %{_slibdir32}/lib*.so
%dir %{_libdir}/gcc/*/*/32
%{_libdir}/gcc/*/*/32/crt*.o
%{_libdir}/gcc/*/*/32/libgcov.a
%{_libdir}/gcc/*/*/32/libgcc.a
%{_libdir}/gcc/*/*/32/libgcc_eh.a
%{_libdir32}/libssp.a
%{_libdir32}/libssp.la
%attr(755,root,root) %{_libdir32}/libssp.so
%{_libdir32}/libssp_nonshared.a
%{_libdir32}/libssp_nonshared.la
%endif

%files -n libgcc
%defattr(644,root,root,755)
%attr(755,root,root) %{_slibdir}/lib*.so.*

%if %{with multilib}
%files -n libgcc-multilib
%defattr(644,root,root,755)
%attr(755,root,root) %{_slibdir32}/lib*.so.*
%endif

%if %{with gomp}
%files -n libgomp
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgomp.so.*.*.*

%if %{with multilib}
%files -n libgomp-multilib
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir32}/libgomp.so.*.*.*
%endif

%files -n libgomp-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgomp.so
%{_libdir}/libgomp.la
%{_libdir}/libgomp.spec
%{_libdir}/gcc/*/*/finclude
%{_infodir}/libgomp*

%if %{with multilib}
%files -n libgomp-multilib-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir32}/libgomp.so
%{_libdir32}/libgomp.la
%{_libdir32}/libgomp.spec
%endif

%files -n libgomp-static
%defattr(644,root,root,755)
%{_libdir}/libgomp.a

%if %{with multilib}
%files -n libgomp-multilib-static
%defattr(644,root,root,755)
%{_libdir32}/libgomp.a
%endif
%endif

%if %{with mudflap}
%files -n libmudflap
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmudflap*.so.*.*.*

%if %{with multilib}
%files -n libmudflap-multilib
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir32}/libmudflap*.so.*.*.*
%endif

%files -n libmudflap-devel
%defattr(644,root,root,755)
%{_libdir}/gcc/*/*/include/mf-runtime.h
%{_libdir}/libmudflap*.la
%attr(755,root,root) %{_libdir}/libmudflap*.so

%if %{with multilib}
%files -n libmudflap-multilib-devel
%defattr(644,root,root,755)
%{_libdir32}/libmudflap*.la
%attr(755,root,root) %{_libdir32}/libmudflap*.so
%endif

%files -n libmudflap-static
%defattr(644,root,root,755)
%{_libdir}/libmudflap*.a

%if %{with multilib}
%files -n libmudflap-multilib-static
%defattr(644,root,root,755)
%{_libdir32}/libmudflap*.a
%endif
%endif

%if %{with ada}
%files ada
%defattr(644,root,root,755)
%doc gcc/ada/ChangeLog
%attr(755,root,root) %{_bindir}/gnat*
%if %{with java}
%exclude %{_bindir}/gnative2ascii
%endif
%attr(755,root,root) %{_libdir}/libgnarl*.so
%attr(755,root,root) %{_libdir}/libgnat*.so
%attr(755,root,root) %{_libdir}/gcc/*/*/gnat1
%{_libdir}/gcc/*/*/adainclude
%dir %{_libdir}/gcc/*/*/adalib
%{_libdir}/gcc/*/*/adalib/*.ali
%{_libdir}/gcc/*/*/adalib/g-trasym.o
%{_libdir}/gcc/*/*/adalib/libgccprefix.a
%ifarch %{ix86} %{x8664}
%{_libdir}/gcc/*/*/adalib/libgmem.a
%endif
%{_infodir}/gnat*

%if %{with multilib}
%files ada-multilib
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir32}/libgnarl*.so
%attr(755,root,root) %{_libdir32}/libgnat*.so
%{_libdir}/gcc/*/*/32/adainclude
%dir %{_libdir}/gcc/*/*/32/adalib
%{_libdir}/gcc/*/*/32/adalib/*.ali
%{_libdir}/gcc/*/*/32/adalib/g-trasym.o
%{_libdir}/gcc/*/*/32/adalib/libgccprefix.a
%ifarch %{ix86} %{x8664}
%{_libdir}/gcc/*/*/32/adalib/libgmem.a
%endif
%endif

%files -n libgnat
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgnarl*.so.1
%attr(755,root,root) %{_libdir}/libgnat*.so.1

%if %{with multilib}
%files -n libgnat-multilib
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir32}/libgnarl*.so.1
%attr(755,root,root) %{_libdir32}/libgnat*.so.1
%endif

%files -n libgnat-static
%defattr(644,root,root,755)
%{_libdir}/gcc/*/*/adalib/libgnala.a
%{_libdir}/gcc/*/*/adalib/libgnarl.a
%{_libdir}/gcc/*/*/adalib/libgnat.a

%if %{with multilib}
%files -n libgnat-multilib-static
%defattr(644,root,root,755)
%{_libdir}/gcc/*/*/32/adalib/libgnala.a
%{_libdir}/gcc/*/*/32/adalib/libgnarl.a
%{_libdir}/gcc/*/*/32/adalib/libgnat.a
%endif
%endif

%if %{with cxx}
%files c++
%defattr(644,root,root,755)
%doc gcc/cp/{ChangeLog,NEWS}
%attr(755,root,root) %{_bindir}/g++
%attr(755,root,root) %{_bindir}/*-g++
%attr(755,root,root) %{_bindir}/c++
%attr(755,root,root) %{_bindir}/*-c++
%attr(755,root,root) %{_libdir}/gcc/*/*/cc1plus
%{_libdir}/libsupc++.a
%{_libdir}/libsupc++.la
%{_mandir}/man1/g++.1*

%if %{with multilib}
%files c++-multilib
%defattr(644,root,root,755)
%{_libdir32}/libsupc++.a
%{_libdir32}/libsupc++.la
%endif

%files -n libstdc++ -f libstdc++.lang
%defattr(644,root,root,755)
%doc libstdc++-v3/{ChangeLog,README}
%attr(755,root,root) %{_libdir}/libstdc++.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libstdc++.so.6

%if %{with multilib}
%files -n libstdc++-multilib
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir32}/libstdc++.so.*.*.*
%attr(755,root,root) %ghost %{_libdir32}/libstdc++.so.6
%endif

%files -n libstdc++-devel
%defattr(644,root,root,755)
%doc libstdc++-v3/doc/html
%dir %{_includedir}/c++
%{_includedir}/c++/%{version}
%{_includedir}/extc++.h
%{_includedir}/stdc++.h
%{_includedir}/stdtr1c++.h
%if %{with java}
%exclude %{_includedir}/c++/%{version}/java
%exclude %{_includedir}/c++/%{version}/javax
%exclude %{_includedir}/c++/%{version}/gcj
%exclude %{_includedir}/c++/%{version}/gnu
%exclude %{_includedir}/c++/%{version}/org
%exclude %{_includedir}/c++/%{version}/sun
%endif
%{_libdir}/libstdc++.la
%attr(755,root,root) %{_libdir}/libstdc++.so

%if %{with multilib}
%files -n libstdc++-multilib-devel
%defattr(644,root,root,755)
%{_libdir32}/libstdc++.la
%attr(755,root,root) %{_libdir32}/libstdc++.so
%endif

%files -n libstdc++-static
%defattr(644,root,root,755)
%{_libdir}/libstdc++.a

%if %{with multilib}
%files -n libstdc++-multilib-static
%defattr(644,root,root,755)
%{_libdir32}/libstdc++.a
%endif
%endif

%if %{with fortran}
%files fortran
%defattr(644,root,root,755)
%doc gcc/fortran/ChangeLog
%attr(755,root,root) %{_bindir}/g95
%attr(755,root,root) %{_bindir}/gfortran
%attr(755,root,root) %{_bindir}/*-gfortran
%{_infodir}/gfortran*
%attr(755,root,root) %{_libdir}/gcc/*/*/f951
%{_libdir}/gcc/*/*/libgfortranbegin.a
%{_libdir}/gcc/*/*/libgfortranbegin.la
%{_libdir}/libgfortran.la
%attr(755,root,root) %{_libdir}/libgfortran.so
%{_mandir}/man1/g95.1*
%{_mandir}/man1/gfortran.1*

%if %{with multilib}
%files fortran-multilib
%defattr(644,root,root,755)
%{_libdir}/gcc/*/*/32/libgfortranbegin.a
%{_libdir}/gcc/*/*/32/libgfortranbegin.la
%{_libdir32}/libgfortran.la
%attr(755,root,root) %{_libdir32}/libgfortran.so
%endif

%files -n libgfortran
%defattr(644,root,root,755)
%doc libgfortran/{AUTHORS,README,ChangeLog}
%attr(755,root,root) %{_libdir}/libgfortran.so.*.*.*

%if %{with multilib}
%files -n libgfortran-multilib
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir32}/libgfortran.so.*.*.*
%endif

%files -n libgfortran-static
%defattr(644,root,root,755)
%{_libdir}/libgfortran.a

%if %{with multilib}
%files -n libgfortran-multilib-static
%defattr(644,root,root,755)
%{_libdir32}/libgfortran.a
%endif
%endif

%if %{with java}
%files java
%defattr(644,root,root,755)
%doc gcc/java/ChangeLog java-doc/*
%attr(755,root,root) %{_bindir}/gappletviewer
%attr(755,root,root) %{_bindir}/gc-analyze
%attr(755,root,root) %{_bindir}/gcj*
%attr(755,root,root) %{_bindir}/gjar
%attr(755,root,root) %{_bindir}/gjarsigner
%attr(755,root,root) %{_bindir}/gjavah
%attr(755,root,root) %{_bindir}/gkeytool
%attr(755,root,root) %{_bindir}/gnative2ascii
%attr(755,root,root) %{_bindir}/gorbd
%attr(755,root,root) %{_bindir}/grmi*
%attr(755,root,root) %{_bindir}/gserialver
%attr(755,root,root) %{_bindir}/gtnameserv
%attr(755,root,root) %{_bindir}/jcf-dump
%attr(755,root,root) %{_bindir}/jv-*
%attr(755,root,root) %{_bindir}/*-gcj*
%attr(755,root,root) %{_libdir}/gcc/*/*/ecj1
%attr(755,root,root) %{_libdir}/gcc/*/*/jc1
%attr(755,root,root) %{_libdir}/gcc/*/*/jvgenmain
%{_infodir}/cp-tools*
%{_infodir}/gcj*
%{_mandir}/man1/gappletviewer*
%{_mandir}/man1/gc-analyze*
%{_mandir}/man1/gcj*
%{_mandir}/man1/gjar*
%{_mandir}/man1/gjavah*
%{_mandir}/man1/gkeytool*
%{_mandir}/man1/gnative2ascii*
%{_mandir}/man1/gorbd*
%{_mandir}/man1/grmi*
%{_mandir}/man1/gserialver*
%{_mandir}/man1/gtnameserv*
%{_mandir}/man1/jcf-*
%{_mandir}/man1/jv-*
%{_mandir}/man1/rebuild-gcj-db*

%files -n libgcj
%defattr(644,root,root,755)
%doc libjava/{ChangeLog,LIBGCJ_LICENSE,NEWS,README,THANKS}
%attr(755,root,root) %{_bindir}/gij
%attr(755,root,root) %{_libdir}/libgcj-tools.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgcj-tools.so.10
%attr(755,root,root) %{_libdir}/libgcj.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgcj.so.10
%attr(755,root,root) %{_libdir}/libgcj_bc.so
%attr(755,root,root) %{_libdir}/libgcj_bc.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgcj_bc.so.1
%attr(755,root,root) %{_libdir}/libgij.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgij.so.10
%{?with_x:%attr(755,root,root) %{_libdir}/lib-gnu-awt-xlib.so.*.*.*}
%{?with_x:%attr(755,root,root) %ghost %{_libdir}/lib-gnu-awt-xlib.so.10}
%dir %{_libdir}/%{gcjdbexecdir}
%{_libdir}/%{gcjdbexecdir}/classmap.db
%{?with_mozilla:%attr(755,root,root) %{_libdir}/%{gcjdbexecdir}/libgcjwebplugin.so}
%{?with_alsa:%attr(755,root,root) %{_libdir}/%{gcjdbexecdir}/libgjsmalsa.so*}
%{?with_dssi:%attr(755,root,root) %{_libdir}/%{gcjdbexecdir}/libgjsmdssi.so*}
%{?with_gtk:%attr(755,root,root) %{_libdir}/%{gcjdbexecdir}/libgtkpeer.so}
%{?with_gtk:%attr(755,root,root) %{_libdir}/%{gcjdbexecdir}/libjawt.so}
%attr(755,root,root) %{_libdir}/%{gcjdbexecdir}/libjavamath.so
%attr(755,root,root) %{_libdir}/%{gcjdbexecdir}/libjvm.so
%{?with_qt:%attr(755,root,root) %{_libdir}/%{gcjdbexecdir}/libqtpeer.so}
%attr(755,root,root) %{_libdir}/%{gcjdbexecdir}/libxmlj.so*
%{_libdir}/logging.properties
%{_javadir}/libgcj*.jar
%{_javadir}/ecj.jar
%{_mandir}/man1/gij*

%files -n libgcj-devel
%defattr(644,root,root,755)
%{_includedir}/c++/%{version}/java
%{_includedir}/c++/%{version}/javax
%{_includedir}/c++/%{version}/gcj
%{_includedir}/c++/%{version}/gnu
%{_includedir}/c++/%{version}/org
%{_includedir}/c++/%{version}/sun
%{_libdir}/gcc/*/*/include/gcj
%{_libdir}/gcc/*/*/include/jawt.h
%{_libdir}/gcc/*/*/include/jawt_md.h
%{_libdir}/gcc/*/*/include/jni.h
%{_libdir}/gcc/*/*/include/jni_md.h
%{_libdir}/gcc/*/*/include/jvmpi.h
%{?with_alsa:%{_libdir}/%{gcjdbexecdir}/libgjsmalsa.la}
%{?with_dssi:%{_libdir}/%{gcjdbexecdir}/libgjsmdssi.la}
%{?with_gtk:%{_libdir}/%{gcjdbexecdir}/libgtkpeer.la}
%{?with_gtk:%{_libdir}/%{gcjdbexecdir}/libjawt.la}
%{_libdir}/%{gcjdbexecdir}/libjavamath.la
%{_libdir}/%{gcjdbexecdir}/libjvm.la
%{?with_qt:%{_libdir}/%{gcjdbexecdir}/libqtpeer.la}
%{?with_mozilla:%{_libdir}/%{gcjdbexecdir}/libgcjwebplugin.la}
%{_libdir}/%{gcjdbexecdir}/libxmlj.la
%dir %{_libdir}/security
%{_libdir}/security/*
%{_libdir}/libgcj.spec
%{_libdir}/libgcj-tools.la
%attr(755,root,root) %{_libdir}/libgcj-tools.so
%{_libdir}/libgcj.la
%attr(755,root,root) %{_libdir}/libgcj.so
%{_libdir}/libgij.la
%attr(755,root,root) %{_libdir}/libgij.so
%if %{with x}
%attr(755,root,root) %{_libdir}/lib-gnu-awt-xlib.so
%{_libdir}/lib-gnu-awt-xlib.la
%endif
%{_pkgconfigdir}/libgcj-%{major_ver}.pc

%files -n libgcj-static
%defattr(644,root,root,755)
%{_libdir}/%{gcjdbexecdir}/libjvm.a
%{_libdir}/libgcj-tools.a
%{_libdir}/libgcj.a
%{_libdir}/libgcj_bc.a
%{_libdir}/libgij.a
%{?with_x:%{_libdir}/lib-gnu-awt-xlib.a}

%files -n libffi
%defattr(644,root,root,755)
%doc libffi/{ChangeLog,ChangeLog.libgcj,LICENSE,README}
%attr(755,root,root) %{_libdir}/libffi.so.*.*.*

%if %{with multilib}
%files -n libffi-multilib
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir32}/libffi.so.*.*.*
%endif

%files -n libffi-devel
%defattr(644,root,root,755)
%{_libdir}/gcc/*/*/include/ffi.h
%{_libdir}/gcc/*/*/include/ffitarget.h
%attr(755,root,root) %{_libdir}/libffi.so
%{_libdir}/libffi.la

%if %{with multilib}
%files -n libffi-multilib-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir32}/libffi.so
%{_libdir32}/libffi.la
%endif

%files -n libffi-static
%defattr(644,root,root,755)
%{_libdir}/libffi.a

%if %{with multilib}
%files -n libffi-multilib-static
%defattr(644,root,root,755)
%{_libdir32}/libffi.a
%endif
%endif

%if %{with objc}
%files objc
%defattr(644,root,root,755)
%doc gcc/objc/README
%attr(755,root,root) %{_libdir}/gcc/*/*/cc1obj
%attr(755,root,root) %{_libdir}/libobjc.so
%{_libdir}/libobjc.la
%{_libdir}/gcc/*/*/include/objc

%if %{with multilib}
%files objc-multilib
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir32}/libobjc.so
%{_libdir32}/libobjc.la
%endif

%files -n libobjc
%defattr(644,root,root,755)
%doc libobjc/{ChangeLog,README*}
%attr(755,root,root) %{_libdir}/libobjc.so.*.*.*

%if %{with multilib}
%files -n libobjc-multilib
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir32}/libobjc.so.*.*.*
%endif

%files -n libobjc-static
%defattr(644,root,root,755)
%{_libdir}/libobjc.a

%if %{with multilib}
%files -n libobjc-multilib-static
%defattr(644,root,root,755)
%{_libdir32}/libobjc.a
%endif
%endif

%if %{with objcxx}
%files objc++
%defattr(644,root,root,755)
%doc gcc/objcp/ChangeLog
%attr(755,root,root) %{_libdir}/gcc/*/*/cc1objplus
%endif
