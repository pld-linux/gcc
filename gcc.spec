#
# TODO:
#	/usr/include/omp.h
#   <multilib>
#	/usr/lib/libgomp.a
#	/usr/lib/libgomp.la
#	/usr/lib/libgomp.so.1.0.0
#   </multilib>
#	/usr/lib/libgomp.spec
#	/usr/lib64/gcj-4.2.0/libxmlj.la
#	/usr/lib64/gcj-4.2.0/libxmlj.so.0.0.0
#	/usr/lib64/libgcj_bc.a
#	/usr/lib64/libgcj_bc.so
#	/usr/lib64/libgcj_bc.so.1.0.0
#	/usr/lib64/libgomp.a
#	/usr/lib64/libgomp.la
#	/usr/lib64/libgomp.so.1.0.0
#	/usr/lib64/libgomp.spec
#	/usr/share/classpath/tools/tools.zip
#
# Conditional build:
%bcond_without	ada		# build without ADA support
%bcond_without	cxx		# build without C++ support
%bcond_without	fortran		# build without Fortran support
%bcond_without	java		# build without Java support
%bcond_without	objc		# build without Objective-C support
%bcond_without	objcxx		# build without Objective-C++ support
%bcond_with	multilib	# build with multilib support (it needs glibc[32&64]-devel)
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

%ifnarch %{x8664} ppc64 s390x sparc64
%undefine	with_multilib
%endif

Summary:	GNU Compiler Collection: the C compiler and shared files
Summary(es):	Colección de compiladores GNU: el compilador C y ficheros compartidos
Summary(pl):	Kolekcja kompilatorów GNU: kompilator C i pliki wspó³dzielone
Summary(pt_BR):	Coleção dos compiladores GNU: o compilador C e arquivos compartilhados
Name:		gcc
%define		_major_ver	4.2
%define		_minor_ver	0
Version:	%{_major_ver}.%{_minor_ver}
%define		_snap	20061021r117925
Release:	0.%{_snap}.1
#Release:	2
Epoch:		5
License:	GPL v2+
Group:		Development/Languages
#Source0:	ftp://gcc.gnu.org/pub/gcc/prerelease-%{version}-%{_snap}/gcc-%{version}-%{_snap}.tar.bz2
#Source0:	ftp://gcc.gnu.org/pub/gcc/releases/gcc-%{version}/%{name}-%{version}.tar.bz2
#Source0:	ftp://gcc.gnu.org/pub/gcc/snapshots/4.1-%{_snap}/gcc-4.1-%{_snap}.tar.bz2
Source0:	gcc-4.2-%{_snap}.tar.bz2
# Source0-md5:	c4bf499f1fd2f8534e6ef65b5bf22c80
Source1:	%{name}-optimize-la.pl
Patch0:		%{name}-info.patch
Patch1:		%{name}-nolocalefiles.patch
Patch2:		%{name}-nodebug.patch
Patch3:		%{name}-ada-link.patch
Patch4:		%{name}-sparc64-ada_fix.patch
Patch5:		%{name}-alpha-ada_fix.patch
Patch6:		%{name}-ppc64-m32-m64-multilib-only.patch
Patch7:		%{name}-libjava-multilib.patch
Patch8:		%{name}-enable-java-awt-qt.patch
Patch9:		%{name}-pr13676.patch
Patch10:	%{name}-pr17390.patch
Patch11:	%{name}-pr19505.patch
Patch12:	%{name}-pr20218.patch
Patch13:	%{name}-pr24669.patch
Patch14:	%{name}-force_jar_wrapper.patch
URL:		http://gcc.gnu.org/
BuildRequires:	autoconf
%{?with_tests:BuildRequires:	autogen}
BuildRequires:	automake
# binutils 2.16.91 or newer are required for compiling medium model now
BuildRequires:	binutils >= 2:2.16.91.0.1
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
BuildRequires:	glibc-devel(sparc)
%endif
%endif
BuildRequires:	perl-base
BuildRequires:	rpmbuild(macros) >= 1.211
BuildRequires:	texinfo >= 4.1
BuildRequires:	zlib-devel
%if %{with fortran}
BuildRequires:	gmp-devel
BuildRequires:	mpfr-devel
%endif
%if %{with java}
BuildRequires:	QtGui-devel >= 4.0.1
BuildRequires:	alsa-lib-devel
BuildRequires:	cairo-devel >= 0.5.0
BuildRequires:	dssi
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	gtk+2-devel >= 2:2.4.0
BuildRequires:	libart_lgpl-devel >= 2.1
BuildRequires:	libxslt-devel
BuildRequires:	pango-devel
BuildRequires:	pkgconfig
BuildRequires:	qt4-build
BuildRequires:	xorg-lib-libXtst-devel
BuildRequires:	zip
BuildRequires:	unzip
%endif
# AS_NEEDED directive for dynamic linker
# http://sources.redhat.com/ml/glibc-cvs/2005-q1/msg00614.html
# http://sources.redhat.com/ml/binutils/2005-01/msg00288.html
Requires:	binutils >= 2:2.16.90.0.1-0.3
Requires:	libgcc = %{epoch}:%{version}-%{release}
Provides:	cpp = %{epoch}:%{version}-%{release}
%{?with_ada:Provides:	gcc(ada)}
%{?with_multilib:Provides:	gcc(multilib)}
Obsoletes:	cpp
Obsoletes:	egcs-cpp
Obsoletes:	gcc-chill
Obsoletes:	gcc-cpp
Obsoletes:	gcc-ksi
Obsoletes:	gont
Conflicts:	glibc-devel < 2.2.5-20
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_slibdir	/%{_lib}
%if %{with multilib}
# 32-bit environment on x86-64,ppc64,s390x,sparc64
%define		_slibdir32	/lib
%define		_libdir32	/usr/lib
%endif

%define		filterout	-fwrapv -fno-strict-aliasing

%description
A compiler aimed at integrating all the optimizations and features
necessary for a high-performance and stable development environment.

This package contains the C compiler and some files shared by various
parts of the GNU Compiler Collection. In order to use another GCC
compiler you will need to install the appropriate subpackage.

%description -l es
Un compilador que intenta integrar todas las optimalizaciones y
características necesarias para un entorno de desarrollo eficaz y
estable.

Este paquete contiene el compilador de C y unos ficheros compartidos
por varias partes de la colección de compiladores GNU (GCC). Para usar
otro compilador de GCC será necesario que instale el subpaquete
adecuado.

%description -l pl
Kompilator, posiadaj±cy du¿e mo¿liwo¶ci optymalizacyjne niezbêdne do
wyprodukowania szybkiego i stabilnego kodu wynikowego.

Ten pakiet zawiera kompilator C i pliki wspó³dzielone przez ró¿ne
czê¶ci kolekcji kompilatorów GNU (GCC). ¯eby u¿ywaæ innego kompilatora
z GCC, trzeba zainstalowaæ odpowiedni podpakiet.

%description -l pt_BR
Este pacote adiciona infraestrutura básica e suporte a linguagem C ao
GNU Compiler Collection.

%package -n libgcc
Summary:	Shared gcc library
Summary(es):	Biblioteca compartida de gcc
Summary(pl):	Biblioteka gcc
Summary(pt_BR):	Biblioteca runtime para o GCC
License:	GPL with unlimited link permission
Group:		Libraries
Obsoletes:	libgcc1

%description -n libgcc
Shared gcc library.

%description -n libgcc -l es
Biblioteca compartida de gcc.

%description -n libgcc -l pl
Biblioteka dynamiczna gcc.

%description -n libgcc -l pt_BR
Biblioteca runtime para o GCC.

%package -n libmudflap
Summary:	GCC mudflap shared support library
Summary(pl):	Wspó³dzielona biblioteka wspomagaj±ca GCC mudflap
License:	GPL v2+ with unlimited link permission
Group:		Libraries

%description -n libmudflap
The libmudflap libraries are used by GCC for instrumenting pointer and
array dereferencing operations.

%description -n libmudflap -l pl
Biblioteki libmudflap s± u¿ywane przez GCC do obs³ugi operacji
dereferencji wspa¼ników i tablic.

%package -n libmudflap-devel
Summary:	Development files for GCC mudflap library
Summary(pl):	Pliki programistyczne biblioteki GCC mudflap
License:	GPL v2+ with unlimited link permission
Group:		Development/Libraries
Requires:	libmudflap = %{epoch}:%{version}-%{release}

%description -n libmudflap-devel
The libmudflap libraries are used by GCC for instrumenting pointer and
array dereferencing operations. This package contains development
files.

%description -n libmudflap-devel -l pl
Biblioteki libmudflap s± u¿ywane przez GCC do obs³ugi operacji
dereferencji wspa¼ników i tablic. Ten pakiet zawiera pliki
programistyczne.

%package -n libmudflap-static
Summary:	Static GCC mudflap library
Summary(pl):	Statyczna biblioteka GCC mudflap
License:	GPL v2+ with unlimited link permission
Group:		Development/Libraries
Requires:	libmudflap-devel = %{epoch}:%{version}-%{release}

%description -n libmudflap-static
The libmudflap libraries are used by GCC for instrumenting pointer and
array dereferencing operations. This package contains static
libraries.

%description -n libmudflap-static -l pl
Biblioteki libmudflap s± u¿ywane przez GCC do obs³ugi operacji
dereferencji wspa¼ników i tablic. Ten pakiet zawiera biblioteki
statyczne.

%package ada
Summary:	Ada support for gcc
Summary(es):	Soporte de Ada para gcc
Summary(pl):	Obs³uga Ady do gcc
Group:		Development/Languages
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	libgnat = %{epoch}:%{version}-%{release}
Obsoletes:	gcc-gnat
Obsoletes:	gnat-devel

%description ada
This package adds experimental support for compiling Ada programs.

%description ada -l es
Este paquete añade soporte experimental para compilar programas en
Ada.

%description ada -l pl
Ten pakiet dodaje eksperymentalne wsparcie dla kompilacji programów w
Adzie.

%package -n libgnat
Summary:	Ada standard libraries
Summary(es):	Bibliotecas estándares de Ada
Summary(pl):	Biblioteki standardowe dla Ady
License:	GPL v2+ with linking exception
Group:		Libraries
Obsoletes:	gnat
Obsoletes:	libgnat1

%description -n libgnat
This package contains shared libraries needed to run programs written
in Ada.

%description -n libgnat -l es
Este paquete contiene las bibliotecas compartidas necesarias para
ejecutar programas escritos en Ada.

%description -n libgnat -l pl
Ten pakiet zawiera biblioteki potrzebne do uruchamiania programów
napisanych w Adzie.

%package -n libgnat-static
Summary:	Static Ada standard libraries
Summary(pl):	Statyczne biblioteki standardowe dla Ady
License:	GPL v2+ with linking exception
Group:		Development/Libraries
Obsoletes:	gnat-static

%description -n libgnat-static
This package contains static libraries for programs written in Ada.

%description -n libgnat-static -l pl
Ten pakiet zawiera biblioteki statyczne dla programów napisanych w
Adzie.

%package c++
Summary:	C++ support for gcc
Summary(es):	Soporte de C++ para gcc
Summary(pl):	Obs³uga C++ dla gcc
Summary(pt_BR):	Suporte C++ para o gcc
Group:		Development/Languages
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	egcc-c++
Obsoletes:	egcs-c++

%description c++
This package adds C++ support to the GNU Compiler Collection. It
includes support for most of the current C++ specification, including
templates and exception handling. It does not include a standard C++
library, which is available separately.

%description c++ -l de
Dieses Paket enthält die C++-Unterstützung für den
GNU-Compiler-Collection. Es unterstützt die aktuelle
C++-Spezifikation, inkl. Templates und Ausnahmeverarbeitung. Eine
C++-Standard-Library ist nicht enthalten - sie ist getrennt
erhältlich.

%description c++ -l es
Este paquete añade soporte de C++ al GCC (colección de compiladores
GNU). Ello incluye el soporte para la mayoría de la especificación
actual de C++, incluyendo plantillas y manejo de excepciones. No
incluye la biblioteca estándar de C++, la que es disponible separada.

%description c++ -l fr
Ce package ajoute un support C++ a la collection de compilateurs GNU.
Il comprend un support pour la plupart des spécifications actuelles de
C++, dont les modéles et la gestion des exceptions. Il ne comprend pas
une bibliothéque C++ standard, qui est disponible séparément.

%description c++ -l pl
Ten pakiet dodaje obs³ugê C++ do kompilatora gcc. Ma wsparcie dla
du¿ej ilo¶ci obecnych specyfikacji C++, nie zawiera natomiast
standardowych bibliotek C++, które s± w oddzielnym pakiecie.

%description c++ -l pt_BR
Este pacote adiciona suporte C++ para o gcc.

%description c++ -l tr
Bu paket, GNU C derleyicisine C++ desteði ekler. 'Template'ler ve
aykýrý durum iþleme gibi çoðu güncel C++ tanýmlarýna uyar. Standart
C++ kitaplýðý bu pakette yer almaz.

%package -n libstdc++
Summary:	GNU C++ library
Summary(es):	Biblioteca C++ de GNU
Summary(pl):	Biblioteki GNU C++
Summary(pt_BR):	Biblioteca C++ GNU
License:	GPL v2+ with free software exception
Group:		Libraries
Obsoletes:	libg++
Obsoletes:	libstdc++3

%description -n libstdc++
This is the GNU implementation of the standard C++ libraries, along
with additional GNU tools. This package includes the shared libraries
necessary to run C++ applications.

%description -n libstdc++ -l de
Dies ist die GNU-Implementierung der Standard-C++-Libraries mit
weiteren GNU-Tools. Dieses Paket enthält die zum Ausführen von
C++-Anwendungen erforderlichen gemeinsam genutzten Libraries.

%description -n libstdc++ -l es
Este es el soporte de las bibliotecas padrón del C++, junto con
herramientas GNU adicionales. El paquete incluye las bibliotecas
compartidas necesarias para ejecutar aplicaciones C++.

%description -n libstdc++ -l fr
Ceci est l'implémentation GNU des librairies C++ standard, ainsi que
des outils GNU supplémentaires. Ce package comprend les librairies
partagées nécessaires à l'exécution d'application C++.

%description -n libstdc++ -l pl
Pakiet ten zawiera biblioteki bêd±ce implementacj± standardowych
bibliotek C++. Znajduj± siê w nim biblioteki dynamiczne niezbêdne do
uruchomienia aplikacji napisanych w C++.

%description -n libstdc++ -l pt_BR
Este pacote é uma implementação da biblioteca padrão C++ v3, um
subconjunto do padrão ISO 14882.

%description -n libstdc++ -l tr
Bu paket, standart C++ kitaplýklarýnýn GNU gerçeklemesidir ve C++
uygulamalarýnýn koþturulmasý için gerekli kitaplýklarý içerir.

%package -n libstdc++-devel
Summary:	Header files and documentation for C++ development
Summary(de):	Header-Dateien zur Entwicklung mit C++
Summary(es):	Ficheros de cabecera y documentación para desarrollo C++
Summary(fr):	Fichiers d'en-tête et biblitothèques pour développer en C++
Summary(pl):	Pliki nag³ówkowe i dokumentacja do biblioteki standardowej C++
Summary(pt_BR):	Arquivos de inclusão e bibliotecas para o desenvolvimento em C++
Summary(tr):	C++ ile program geliþtirmek için gerekli dosyalar
License:	GPL v2+ with free software exception
Group:		Development/Libraries
Requires:	%{name}-c++ = %{epoch}:%{version}-%{release}
Requires:	libstdc++ = %{epoch}:%{version}-%{release}
Requires:	glibc-devel
Obsoletes:	libg++-devel
Obsoletes:	libstdc++3-devel

%description -n libstdc++-devel
This is the GNU implementation of the standard C++ libraries. This
package includes the header files needed for C++ development and
library documentation.

%description -n libstdc++-devel -l es
Este es el soporte de las bibliotecas padrón del lenguaje C++. Este
paquete incluye los archivos de inclusión y bibliotecas necesarios
para desarrollo de programas en lenguaje C++.

%description -n libstdc++-devel -l pl
Pakiet ten zawiera biblioteki bêd±ce implementacj± standardowych
bibliotek C++. Znajduj± siê w nim pliki nag³ówkowe wykorzystywane przy
programowaniu w jêzyku C++ oraz dokumentacja biblioteki standardowej.

%description -n libstdc++-devel -l pt_BR
Este pacote inclui os arquivos de inclusão e bibliotecas necessárias
para desenvolvimento de programas C++.

%package -n libstdc++-static
Summary:	Static C++ standard library
Summary(es):	Biblioteca estándar estática de C++
Summary(pl):	Statyczna biblioteka standardowa C++
License:	GPL v2+ with free software exception
Group:		Development/Libraries
Requires:	libstdc++-devel = %{epoch}:%{version}-%{release}

%description -n libstdc++-static
Static C++ standard library.

%description -n libstdc++-static -l es
Biblioteca estándar estática de C++.

%description -n libstdc++-static -l pl
Statyczna biblioteka standardowa C++.

%package fortran
Summary:	Fortran 95 support for gcc
Summary(es):	Soporte de Fortran 95 para gcc
Summary(pl):	Obs³uga Fortranu 95 dla gcc
Summary(pt_BR):	Suporte Fortran 95 para o GCC
Group:		Development/Languages/Fortran
Requires:	libgfortran = %{epoch}:%{version}-%{release}
Provides:	gcc-g77 = %{epoch}:%{version}-%{release}
Obsoletes:	egcs-g77
Obsoletes:	gcc-g77

%description fortran
This package adds support for compiling Fortran 95 programs with the
GNU compiler.

%description fortran -l es
Este paquete añade soporte para compilar programas escritos en Fortran
95 con el compilador GNU.

%description fortran -l pl
Ten pakiet dodaje obs³ugê Fortranu 95 do kompilatora gcc. Jest
potrzebny do kompilowania programów pisanych w jêzyku Fortran 95.

%description fortran -l pt_BR
Suporte Fortran 95 para o GCC.

%package -n libgfortran
Summary:	Fortran 95 Libraries
Summary(es):	Bibliotecas de Fortran 95
Summary(pl):	Biblioteki Fortranu 95
License:	LGPL v2+
Group:		Libraries
Obsoletes:	libg2c

%description -n libgfortran
Fortran 95 Libraries.

%description -n libgfortran -l es
Bibliotecas de Fortran 95.

%description -n libgfortran -l pl
Biblioteki Fortranu 95.

%package -n libgfortran-static
Summary:	Static Fortran 95 Libraries
Summary(es):	Bibliotecas estáticas de Fortran 95
Summary(pl):	Statyczne Biblioteki Fortranu 95
License:	LGPL v2+
Group:		Development/Libraries
Requires:	libgfortran = %{epoch}:%{version}-%{release}
Obsoletes:	libg2c-static

%description -n libgfortran-static
Static Fortran 95 Libraries.

%description -n libgfortran-static -l es
Bibliotecas estáticas de Fortran 95.

%description -n libgfortran-static -l pl
Statyczne biblioteki Fortranu 95.

%package java
Summary:	Java support for gcc
Summary(es):	Soporte de Java para gcc
Summary(pl):	Obs³uga Javy dla gcc
Group:		Development/Languages/Java
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	libgcj-devel = %{epoch}:%{version}-%{release}
Provides:	gcj = %{epoch}:%{version}-%{release}
Provides:	gcc-java-tools
Obsoletes:	fastjar
Obsoletes:	gcc-java-tools

%description java
This package adds experimental support for compiling Java(TM) programs
and bytecode into native code. To use this you will also need the
libgcj package.

%description java -l es
Este paquete añade soporte experimental para compilar programas
Java(tm) y su bytecode en código nativo. Para usarlo también va a
necesitar el paquete libgcj.

%description java -l pl
Ten pakiet dodaje mo¿liwo¶æ kompilowania programów w jêzyku Java(TM)
oraz bajtkodu do kodu natywnego. Do u¿ywania go wymagany jest
dodatkowo pakiet libgcj.

%package -n libgcj
Summary:	Java Class Libraries
Summary(es):	Bibliotecas de clases de Java
Summary(pl):	Biblioteki Klas Javy
License:	GPL with limited linking exception
Group:		Libraries
Obsoletes:	libgcj3

%description -n libgcj
Java Class Libraries.

%description -n libgcj -l es
Bibliotecas de clases de Java.

%description -n libgcj -l pl
Biblioteki Klas Javy.

%package -n libgcj-devel
Summary:	Development files for Java Class Libraries
Summary(es):	Ficheros de desarrollo para las bibliotecas de clases de Java
Summary(pl):	Pliki nag³ówkowe dla Bibliotek Klas Javy
License:	GPL with limited linking exception
Group:		Development/Libraries
Requires:	libgcj = %{epoch}:%{version}-%{release}
Requires:	zlib-devel
Obsoletes:	libgcj3-devel

%description -n libgcj-devel
Development files for Java Class Libraries.

%description -n libgcj-devel -l es
Ficheros de desarrollo para las bibliotecas de clases de Java.

%description -n libgcj-devel -l pl
Pliki nag³ówkowe dla Bibliotek Klas Javy.

%package -n libgcj-static
Summary:	Static Java Class Libraries
Summary(es):	Bibliotecas estáticas de clases de Java
Summary(pl):	Statyczne Biblioteki Klas Javy
License:	GPL with limited linking exception
Group:		Development/Libraries
Requires:	libgcj-devel = %{epoch}:%{version}-%{release}
Requires:	libstdc++-devel = %{epoch}:%{version}-%{release}

%description -n libgcj-static
Static Java Class Libraries.

%description -n libgcj-static -l es
Bibliotecas estáticas de clases de Java.

%description -n libgcj-static -l pl
Statyczne Biblioteki Klas Javy.

%package -n libffi
Summary:	Foreign Function Interface library
Summary(es):	Biblioteca de interfaz de funciones ajenas
Summary(pl):	Biblioteka zewnêtrznych wywo³añ funkcji
License:	BSD-like
Group:		Libraries

%description -n libffi
The libffi library provides a portable, high level programming
interface to various calling conventions. This allows a programmer to
call any function specified by a call interface description at run
time.

%description -n libffi -l es
La biblioteca libffi provee una interfaz portable de programación de
alto nivel para varias convenciones de llamada. Ello permite que un
programador llame una función cualquiera especificada por una
descripción de interfaz de llamada en el tiempo de ejecución.

%description -n libffi -l pl
Biblioteka libffi dostarcza przeno¶nego, wysokopoziomowego
miêdzymordzia do ró¿nych konwencji wywo³añ funkcji. Pozwala to
programi¶cie wywo³ywaæ dowolne funkcje podaj±c konwencjê wywo³ania w
czasie wykonania.

%package -n libffi-devel
Summary:	Development files for Foreign Function Interface library
Summary(es):	Ficheros de desarrollo para libffi
Summary(pl):	Pliki nag³ówkowe dla libffi
License:	BSD-like
Group:		Development/Libraries
Requires:	libffi = %{epoch}:%{version}-%{release}

%description -n libffi-devel
Development files for Foreign Function Interface library.

%description -n libffi-devel -l es
Ficheros de desarrollo para libffi.

%description -n libffi-devel -l pl
Pliki nag³ówkowe dla libffi.

%package -n libffi-static
Summary:	Static Foreign Function Interface library
Summary(es):	Biblioteca libffi estática
Summary(pl):	Statyczna biblioteka libffi
License:	BSD-like
Group:		Development/Libraries
Requires:	libffi-devel = %{epoch}:%{version}-%{release}

%description -n libffi-static
Static Foreign Function Interface library.

%description -n libffi-static -l es
Biblioteca libffi estática.

%description -n libffi-static -l pl
Statyczna biblioteka libffi.

%package objc
Summary:	Objective C support for gcc
Summary(de):	Objektive C-Unterstützung für gcc
Summary(es):	Soporte de Objective C para gcc
Summary(fr):	Gestion d'Objective C pour gcc
Summary(pl):	Obs³uga obiektowego C dla kompilatora gcc
Summary(tr):	gcc için Objective C desteði
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

%description objc -l de
Dieses Paket ergänzt den GNU-Compiler-Collection durch
Objective-C-Support. Objective C ist ein objektorientiertes Derivat
von C, das zur Hauptsache auf Systemen mit NeXTSTEP zum Einsatz kommt.
Die Standard-Objective-C-Objekt-Library ist nicht Teil des Pakets.

%description objc -l es
Este paquete añade soporte de Objective C al GCC (colección de
compiladores GNU). Objective C es un lenguaje orientado a objetos
derivado de C, principalmente usado en sistemas que funcionan bajo
NeXTSTEP. El paquete no incluye la biblioteca de objetos estándar de
Objective C.

%description objc -l fr
Ce package ajoute un support Objective C a la collection de
compilateurs GNU. L'Objective C est un langage orienté objetdérivé du
langage C, principalement utilisé sur les systèmes NeXTSTEP. Ce
package n'inclue pas la bibliothéque Objective C standard.

%description objc -l pl
Ten pakiet dodaje obs³ugê obiektowego C do kompilatora gcc. Obiektowe
C (objc) jest zorientowan± obiektowo pochodn± jêzyka C, u¿ywan±
g³ównie w systemach u¿ywaj±cych NeXTSTEP. W pakiecie nie ma
standardowej biblioteki objc (która znajduje siê w osobnym pakiecie).

%description objc -l tr
Bu paket, GNU C derleyicisine Objective C desteði ekler. Objective C,
C dilinin nesne yönelik bir türevidir ve NeXTSTEP altýnda çalýþan
sistemlerde yaygýn olarak kullanýlýr. Standart Objective C nesne
kitaplýðý bu pakette yer almaz.

%package objc++
Summary:	Objective C++ support for gcc
Summary(pl):	Obs³uga jêzyka Objective C++ dla gcc
Group:		Development/Languages
Requires:	%{name}-c++ = %{epoch}:%{version}-%{release}
Requires:	%{name}-objc = %{epoch}:%{version}-%{release}

%description objc++
This package adds Objective C++ support to the GNU Compiler
Collection.

%description objc++ -l pl
Ten pakiet dodaje obs³ugê jêzyka Objective C++ do zestawu
kompilatorów GNU Compiler Collection.

%package -n libobjc
Summary:	Objective C Libraries
Summary(es):	Bibliotecas de Objective C
Summary(pl):	Biblioteki Obiektowego C
License:	GPL v2+ with linking exception
Group:		Libraries
Obsoletes:	libobjc1

%description -n libobjc
Objective C Libraries.

%description -n libobjc -l es
Bibliotecas de Objective C.

%description -n libobjc -l pl
Biblioteki Obiektowego C.

%package -n libobjc-static
Summary:	Static Objective C Libraries
Summary(es):	Bibliotecas estáticas de Objective C
Summary(pl):	Statyczne Biblioteki Obiektowego C
License:	GPL v2+ with linking exception
Group:		Development/Libraries
Requires:	libobjc = %{epoch}:%{version}-%{release}

%description -n libobjc-static
Static Objective C Libraries.

%description -n libobjc-static -l es
Bibliotecas estáticas de Objective C.

%description -n libobjc-static -l pl
Statyczne biblioteki Obiektowego C.

%prep
#setup -q -n gcc-%{version}
%setup -q -n gcc-4_2-branch
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
#patch10 -p1	not quite correct / temp. disabled.
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1

# because we distribute modified version of gcc...
sed -i 's:#define VERSUFFIX.*:#define VERSUFFIX " (PLD-Linux)":' gcc/version.c
perl -pi -e 's@(bug_report_url.*<URL:).*";@$1http://bugs.pld-linux.org/>";@' gcc/version.c

mv ChangeLog ChangeLog.general

%build
cd gcc
%{__autoconf}
cd ..
cd libjava
%{__autoconf}
cd classpath
%{__autoconf}
cd ../..
cp -f /usr/share/automake/config.sub .

rm -rf builddir && install -d builddir && cd builddir

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
	--enable-languages="c%{?with_cxx:,c++}%{?with_fortran:,fortran}%{?with_objc:,objc}%{?with_objcxx:,obj-c++}%{?with_ada:,ada}%{?with_java:,java}" \
	--enable-c99 \
	--enable-long-long \
	--%{?with_multilib:en}%{!?with_multilib:dis}able-multilib \
	--enable-nls \
	--disable-werror \
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
	--with-gxx-include-dir=%{_includedir}/c++ \
	--disable-libstdcxx-pch \
	--enable-__cxa_atexit \
	--enable-libstdcxx-allocator=new \
%endif
%if %{with java}
	--disable-libjava-multilib \
	--enable-libgcj \
	--enable-libgcj-multifile \
	--enable-libgcj-database \
	--enable-gtk-cairo \
	--enable-java-awt=qt,gtk,xlib \
	--enable-jni \
	--enable-xmlj \
	--enable-alsa \
	--enable-dssi \
%endif
	--%{?with_bootstrap:en}%{!?with_bootstrap:dis}able-bootstrap \
	%{_target_platform}

cd ..

%{__make} -C builddir \
	%{?with_bootstrap:%{?with_profiling:profiledbootstrap}} \
	GCJFLAGS="%{rpmcflags}" \
	BOOT_CFLAGS="%{rpmcflags}" \
	STAGE1_CFLAGS="%{rpmcflags} -O0" \
	GNATLIBCFLAGS="%{rpmcflags}" \
	LDFLAGS_FOR_TARGET="%{rpmldflags}" \
	mandir=%{_mandir} \
	infodir=%{_infodir}

%{?with_tests:%{__make} -k -C builddir check 2>&1 ||:}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/lib,%{_aclocaldir},%{_datadir},%{_infodir}}

cd builddir

%{__make} -j1 install \
	mandir=%{_mandir} \
	infodir=%{_infodir} \
	DESTDIR=$RPM_BUILD_ROOT

install gcc/specs $RPM_BUILD_ROOT%{_libdir}/gcc/%{_target_platform}/%{version}

%ifarch sparc64
ln -sf	%{_bindir}/sparc64-pld-linux-gcc \
	$RPM_BUILD_ROOT%{_bindir}/sparc-pld-linux-gcc
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
test -f	$RPM_BUILD_ROOT%{_libdir}/libgnat-4.2.so.1
ln -sf	libgnat-4.2.so.1 $RPM_BUILD_ROOT%{_libdir}/libgnat-4.2.so
ln -sf	libgnarl-4.2.so.1 $RPM_BUILD_ROOT%{_libdir}/libgnarl-4.2.so
ln -sf	libgnat-4.2.so $RPM_BUILD_ROOT%{_libdir}/libgnat.so
ln -sf	libgnarl-4.2.so $RPM_BUILD_ROOT%{_libdir}/libgnarl.so
%endif

cd ..

%if %{with java}
install -d java-doc
cp -f	libjava/READ* java-doc
ln -sf	%{_javadir}/libgcj-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/libgcj.jar
rm -f $RPM_BUILD_ROOT%{_libdir}/classpath/libgjs*.la
# tools.zip sources
rm -rf $RPM_BUILD_ROOT%{_datadir}/classpath/tools/gnu
%endif
%if %{with objc}
cp -f	libobjc/README gcc/objc/README.libobjc
%endif

# avoid -L poisoning in *.la - there should be only -L%{_libdir}/gcc/*/%{version}
# normalize libdir, to avoid propagation of unnecessary RPATHs by libtool
for f in libgomp.la libmudflap.la libmudflapth.la libssp.la libssp_nonshared.la \
	%{?with_cxx:libstdc++.la libsupc++.la} \
	%{?with_fortran:libgfortran.la} \
%if %{with java}
	libgcj.la libgcj-tools.la libffi.la lib-gnu-awt-xlib.la \
	gcj-%{version}/libgtkpeer.la gcj-%{version}/libjawt.la gcj-%{version}/libjvm.la gcj-%{version}/libqtpeer.la \
	gcj-%{version}/libgjsmalsa.la gcj-%{version}/libgjsmdssi.la gcj-%{version}/libxmlj.la \
%endif
	%{?with_objc:libobjc.la};
do
	%{SOURCE1} $RPM_BUILD_ROOT%{_libdir}/$f %{_libdir} > $RPM_BUILD_ROOT%{_libdir}/$f.fixed
	mv $RPM_BUILD_ROOT%{_libdir}/$f{.fixed,}
done
%if %{with multilib}
for f in libgomp.la libmudflap.la libmudflapth.la libssp.la libssp_nonshared.la \
	%{?with_cxx:libstdc++.la libsupc++.la} \
	%{?with_fortran:libgfortran.la} \
	%{?with_java:libffi.la} \
	%{?with_objc:libobjc.la};
do
	%{SOURCE1} $RPM_BUILD_ROOT%{_libdir32}/$f %{_libdir32} > $RPM_BUILD_ROOT%{_libdir32}/$f.fixed
	mv $RPM_BUILD_ROOT%{_libdir32}/$f{.fixed,}
done
%endif

# include/ contains install-tools/include/* and headers that were fixed up
# by fixincludes, we don't want former
gccdir=$(echo $RPM_BUILD_ROOT%{_libdir}/gcc/*/*/)
mkdir	$gccdir/tmp

# we have to save these however
%{?with_java:mv $gccdir/include/{gcj,ffi.h,ffitarget.h,jawt.h,jawt_md.h,jni.h,jni_md.h,jvmpi.h} $gccdir/tmp}
%{?with_objc:mv $gccdir/include/objc $gccdir/tmp}
mv $gccdir/include/mf-runtime.h $gccdir/tmp
mv $gccdir/include/syslimits.h $gccdir/tmp
mv $gccdir/include/ssp $gccdir/tmp
rm -rf $gccdir/include
mv $gccdir/tmp $gccdir/include
cp $gccdir/install-tools/include/*.h $gccdir/include
# but we don't want anything more from install-tools
rm -rf $gccdir/install-tools

%find_lang gcc
%find_lang cpplib
cat cpplib.lang >> gcc.lang

%if %{with cxx}
%find_lang libstdc\+\+
install libstdc++-v3/include/precompiled/* $RPM_BUILD_ROOT%{_includedir}
%endif

# cvs snap doesn't contain (release does) below files,
# so let's create dummy entries to satisfy %%files.
[ ! -f NEWS ] && touch NEWS
[ ! -f libgfortran/AUTHORS ] && touch libgfortran/AUTHORS
[ ! -f libgfortran/README ] && touch libgfortran/README

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%post ada
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun ada
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%post fortran
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun fortran
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%post java
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun java
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%post	-p /sbin/ldconfig -n libgcc
%postun	-p /sbin/ldconfig -n libgcc
%post	-p /sbin/ldconfig -n libmudflap
%postun	-p /sbin/ldconfig -n libmudflap
%post	-p /sbin/ldconfig -n libgnat
%postun	-p /sbin/ldconfig -n libgnat
%post	-p /sbin/ldconfig -n libstdc++
%postun	-p /sbin/ldconfig -n libstdc++
%post	-p /sbin/ldconfig -n libgfortran
%postun	-p /sbin/ldconfig -n libgfortran
%post	-p /sbin/ldconfig -n libgcj
%postun	-p /sbin/ldconfig -n libgcj
%post	-p /sbin/ldconfig -n libffi
%postun	-p /sbin/ldconfig -n libffi
%post	-p /sbin/ldconfig -n libobjc
%postun	-p /sbin/ldconfig -n libobjc

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
%if %{with multilib}
%attr(755,root,root) %{_slibdir32}/lib*.so
%dir %{_libdir}/gcc/*/*/32
%{_libdir}/gcc/*/*/32/libgcov.a
%{_libdir}/gcc/*/*/32/libgcc.a
%{_libdir}/gcc/*/*/32/libgcc_eh.a
%{_libdir32}/libssp.a
%{_libdir32}/libssp.la
%attr(755,root,root) %{_libdir32}/libssp.so
%{_libdir32}/libssp_nonshared.a
%{_libdir32}/libssp_nonshared.la
%endif
%{_libdir}/gcc/*/*/libgcov.a
%{_libdir}/gcc/*/*/libgcc.a
%{_libdir}/gcc/*/*/libgcc_eh.a
%{_libdir}/gcc/*/*/specs
%if %{with multilib}
%{_libdir}/gcc/*/*/32/crt*.o
%endif
%{_libdir}/gcc/*/*/crt*.o
%attr(755,root,root) %{_libdir}/gcc/*/*/cc1
%attr(755,root,root) %{_libdir}/gcc/*/*/collect2

%dir %{_libdir}/gcc/*/*/include
%dir %{_libdir}/gcc/*/*/include/ssp
%{_libdir}/gcc/*/*/include/ssp/*.h
%{_libdir}/gcc/*/*/include/decfloat.h
%{_libdir}/gcc/*/*/include/float.h
%{_libdir}/gcc/*/*/include/iso646.h
%{_libdir}/gcc/*/*/include/limits.h
%{_libdir}/gcc/*/*/include/stdarg.h
%{_libdir}/gcc/*/*/include/stdbool.h
%{_libdir}/gcc/*/*/include/stddef.h
%{_libdir}/gcc/*/*/include/syslimits.h
%{_libdir}/gcc/*/*/include/unwind.h
%{_libdir}/gcc/*/*/include/varargs.h
%ifarch %{ix86} %{x8664}
%{_libdir}/gcc/*/*/include/emmintrin.h
%{_libdir}/gcc/*/*/include/mm3dnow.h
%{_libdir}/gcc/*/*/include/mm_malloc.h
%{_libdir}/gcc/*/*/include/mmintrin.h
%{_libdir}/gcc/*/*/include/pmmintrin.h
%{_libdir}/gcc/*/*/include/xmmintrin.h
%endif

%files -n libgcc
%defattr(644,root,root,755)
%if %{with multilib}
%attr(755,root,root) %{_slibdir32}/lib*.so.*
%endif
%attr(755,root,root) %{_slibdir}/lib*.so.*

%files -n libmudflap
%defattr(644,root,root,755)
%if %{with multilib}
%attr(755,root,root) %{_libdir32}/libmudflap*.so.*.*.*
%endif
%attr(755,root,root) %{_libdir}/libmudflap*.so.*.*.*

%files -n libmudflap-devel
%defattr(644,root,root,755)
%{_libdir}/gcc/*/*/include/mf-runtime.h
%if %{with multilib}
%{_libdir32}/libmudflap*.la
%attr(755,root,root) %{_libdir32}/libmudflap*.so
%endif
%{_libdir}/libmudflap*.la
%attr(755,root,root) %{_libdir}/libmudflap*.so

%files -n libmudflap-static
%defattr(644,root,root,755)
%if %{with multilib}
%{_libdir32}/libmudflap*.a
%endif
%{_libdir}/libmudflap*.a

%if %{with ada}
%files ada
%defattr(644,root,root,755)
%doc gcc/ada/ChangeLog
%attr(755,root,root) %{_bindir}/gnat*
%attr(755,root,root) %{_bindir}/gpr*
%attr(755,root,root) %{_libdir}/libgnarl*.so
%attr(755,root,root) %{_libdir}/libgnat*.so
%attr(755,root,root) %{_libdir}/gcc/*/*/gnat1
%{_libdir}/gcc/*/*/adainclude
%dir %{_libdir}/gcc/*/*/adalib
%{_libdir}/gcc/*/*/adalib/*.ali
%{_libdir}/gcc/*/*/adalib/g-trasym.o
%{_libdir}/gcc/*/*/adalib/libgccprefix.a
%ifarch %{ix86}
%{_libdir}/gcc/*/*/adalib/libgmem.a
%endif
%{_infodir}/gnat*

%files -n libgnat
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgnarl*.so.1
%attr(755,root,root) %{_libdir}/libgnat*.so.1

%files -n libgnat-static
%defattr(644,root,root,755)
%{_libdir}/gcc/*/*/adalib/libgnarl.a
%{_libdir}/gcc/*/*/adalib/libgnat.a
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
%if %{with multilib}
%{_libdir32}/libsupc++.a
%{_libdir32}/libsupc++.la
%endif
%{_libdir}/libsupc++.a
%{_libdir}/libsupc++.la
%{_mandir}/man1/g++.1*

%files -n libstdc++ -f libstdc++.lang
%defattr(644,root,root,755)
%doc libstdc++-v3/{ChangeLog,README}
%if %{with multilib}
%attr(755,root,root) %{_libdir32}/libstdc++.so.*.*.*
%endif
%attr(755,root,root) %{_libdir}/libstdc++.so.*.*.*

%files -n libstdc++-devel
%defattr(644,root,root,755)
%doc libstdc++-v3/docs/html
%{_includedir}/c++
%{_includedir}/extc++.h
%{_includedir}/stdc++.h
%{_includedir}/stdtr1c++.h
%if %{with java}
%exclude %{_includedir}/c++/java
%exclude %{_includedir}/c++/javax
%exclude %{_includedir}/c++/gcj
%exclude %{_includedir}/c++/gnu
%endif
%if %{with multilib}
%{_libdir32}/libstdc++.la
%attr(755,root,root) %{_libdir32}/libstdc++.so
%endif
%{_libdir}/libstdc++.la
%attr(755,root,root) %{_libdir}/libstdc++.so

%files -n libstdc++-static
%defattr(644,root,root,755)
%if %{with multilib}
%{_libdir32}/libstdc++.a
%endif
%{_libdir}/libstdc++.a
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
%if %{with multilib}
%{_libdir}/gcc/*/*/32/libgfortranbegin.a
%{_libdir32}/libgfortran.la
%attr(755,root,root) %{_libdir32}/libgfortran.so
%endif
%{_libdir}/libgfortran.la
%attr(755,root,root) %{_libdir}/libgfortran.so
%{_mandir}/man1/g95.1*
%{_mandir}/man1/gfortran.1*

%files -n libgfortran
%defattr(644,root,root,755)
%doc libgfortran/{AUTHORS,README,ChangeLog}
%if %{with multilib}
%attr(755,root,root) %{_libdir32}/libgfortran.so.*.*.*
%endif
%attr(755,root,root) %{_libdir}/libgfortran.so.*.*.*

%files -n libgfortran-static
%defattr(644,root,root,755)
%if %{with multilib}
%{_libdir32}/libgfortran.a
%endif
%{_libdir}/libgfortran.a
%endif

%if %{with java}
%files java
%defattr(644,root,root,755)
%doc gcc/java/ChangeLog java-doc/*
%attr(755,root,root) %{_bindir}/gappletviewer
%attr(755,root,root) %{_bindir}/gcj*
%attr(755,root,root) %{_bindir}/gjarsigner
%attr(755,root,root) %{_bindir}/gjnih
%attr(755,root,root) %{_bindir}/gkeytool
%attr(755,root,root) %{_bindir}/grmi*
%attr(755,root,root) %{_bindir}/jar
%attr(755,root,root) %{_bindir}/jcf-dump
%attr(755,root,root) %{_bindir}/jv-*
%attr(755,root,root) %{_bindir}/*-gcj*
%attr(755,root,root) %{_libdir}/gcc/*/*/jc1
%attr(755,root,root) %{_libdir}/gcc/*/*/jvgenmain
%{_infodir}/gcj*
%{_mandir}/man1/gcj*
%{_mandir}/man1/gjnih*
%{_mandir}/man1/grmi*
%{_mandir}/man1/jcf-*
%{_mandir}/man1/jv-*

%files -n libgcj
%defattr(644,root,root,755)
%doc libjava/{ChangeLog,LIBGCJ_LICENSE,NEWS,README,THANKS}
%attr(755,root,root) %{_bindir}/addr2name.awk
%attr(755,root,root) %{_bindir}/gij
%attr(755,root,root) %{_libdir}/libgcj.so.*.*.*
%attr(755,root,root) %{_libdir}/libgcj-tools.so.*.*.*
%attr(755,root,root) %{_libdir}/libgij.so.*.*.*
%attr(755,root,root) %{_libdir}/lib-gnu-awt-xlib.so.*.*.*
%dir %{_libdir}/gcj-%{version}
%{_libdir}/gcj-%{version}/classmap.db
%attr(755,root,root) %{_libdir}/gcj-%{version}/libgjsmalsa.so*
%attr(755,root,root) %{_libdir}/gcj-%{version}/libgjsmdssi.so*
%attr(755,root,root) %{_libdir}/gcj-%{version}/libgtkpeer.so
%attr(755,root,root) %{_libdir}/gcj-%{version}/libjawt.so
%attr(755,root,root) %{_libdir}/gcj-%{version}/libjvm.so
%attr(755,root,root) %{_libdir}/gcj-%{version}/libqtpeer.so
%{_libdir}/logging.properties
%{_javadir}/libgcj*.jar
%{_mandir}/man1/gij*

%files -n libgcj-devel
%defattr(644,root,root,755)
%{_includedir}/c++/java
%{_includedir}/c++/javax
%{_includedir}/c++/gcj
%{_includedir}/c++/gnu
%{_libdir}/gcc/*/*/include/gcj
%{_libdir}/gcc/*/*/include/jawt.h
%{_libdir}/gcc/*/*/include/jawt_md.h
%{_libdir}/gcc/*/*/include/jni.h
%{_libdir}/gcc/*/*/include/jni_md.h
%{_libdir}/gcc/*/*/include/jvmpi.h
%dir %{_libdir}/security
%{_libdir}/security/*
%{_libdir}/libgcj.spec
%attr(755,root,root) %{_libdir}/libgcj.so
%{_libdir}/libgcj.la
%attr(755,root,root) %{_libdir}/libgcj-tools.so
%{_libdir}/libgcj-tools.la
%attr(755,root,root) %{_libdir}/libgij.so
%{_libdir}/libgij.la
%attr(755,root,root) %{_libdir}/lib-gnu-awt-xlib.so
%{_libdir}/lib-gnu-awt-xlib.la
%{_libdir}/gcj-%{version}/libgjsmalsa.la
%{_libdir}/gcj-%{version}/libgjsmdssi.la
%{_libdir}/gcj-%{version}/libgtkpeer.la
%{_libdir}/gcj-%{version}/libjawt.la
%{_libdir}/gcj-%{version}/libjvm.la
%{_libdir}/gcj-%{version}/libqtpeer.la
%{_pkgconfigdir}/libgcj-%{_major_ver}.pc

%files -n libgcj-static
%defattr(644,root,root,755)
%{_libdir}/libgcj.a
%{_libdir}/libgcj-tools.a
%{_libdir}/libgij.a
%{_libdir}/lib-gnu-awt-xlib.a
%{_libdir}/gcj-%{version}/libjvm.a
# needs check.
#{_libdir}/gcj-%{version}/libgtkpeer.a
#{_libdir}/gcj-%{version}/libjawt.a
#{_libdir}/gcj-%{version}/libqtpeer.a

%files -n libffi
%defattr(644,root,root,755)
%doc libffi/{ChangeLog,ChangeLog.libgcj,LICENSE,README}
%if %{with multilib}
%attr(755,root,root) %{_libdir32}/libffi.so.*.*.*
%endif
%attr(755,root,root) %{_libdir}/libffi.so.*.*.*

%files -n libffi-devel
%defattr(644,root,root,755)
%{_libdir}/gcc/*/*/include/ffi.h
%{_libdir}/gcc/*/*/include/ffitarget.h
%if %{with multilib}
%attr(755,root,root) %{_libdir32}/libffi.so
%{_libdir32}/libffi.la
%endif
%attr(755,root,root) %{_libdir}/libffi.so
%{_libdir}/libffi.la

%files -n libffi-static
%defattr(644,root,root,755)
%if %{with multilib}
%{_libdir32}/libffi.a
%endif
%{_libdir}/libffi.a
%endif

%if %{with objc}
%files objc
%defattr(644,root,root,755)
%doc gcc/objc/README
%attr(755,root,root) %{_libdir}/gcc/*/*/cc1obj
%if %{with multilib}
%attr(755,root,root) %{_libdir32}/libobjc.so
%{_libdir32}/libobjc.la
%endif
%attr(755,root,root) %{_libdir}/libobjc.so
%{_libdir}/libobjc.la
%{_libdir}/gcc/*/*/include/objc

%files -n libobjc
%defattr(644,root,root,755)
%doc libobjc/{ChangeLog,README*}
%if %{with multilib}
%attr(755,root,root) %{_libdir32}/libobjc.so.*.*.*
%endif
%attr(755,root,root) %{_libdir}/libobjc.so.*.*.*

%files -n libobjc-static
%defattr(644,root,root,755)
%if %{with multilib}
%{_libdir32}/libobjc.a
%endif
%{_libdir}/libobjc.a
%endif

%if %{with objcxx}
%files objc++
%defattr(644,root,root,755)
%doc gcc/objcp/ChangeLog
%attr(755,root,root) %{_libdir}/gcc/*/*/cc1objplus
%endif
