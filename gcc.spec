#
# Conditional build:
%bcond_without	ada		# build without ADA support
%bcond_without	cxx		# build without C++ support
%bcond_without	fortran		# build without Fortran77 support
%bcond_without	java		# build without Java support
%bcond_without	ksi		# build without KSI support
%bcond_without	objc		# build without objc support
%bcond_with	bootstrap	# don't BR gcc(ada) (temporary for Ac upgrade bootstrap)
%bcond_with	boot64		# 32->64-bit bootstrap (sparc->sparc64, maybe ppc too?)
%ifarch %{x8664} sparc64
%bcond_without	multilib	# build without multilib support
%else
%bcond_with	multilib	# build with multilib support
%endif
#
%ifnarch %{x8664} ppc64 s390x sparc64
%undefine	with_multilib
%endif
%if %{with boot64}
%undefine	with_ada
%undefine	with_cxx
%undefine	with_fortran
%undefine	with_java
%undefine	with_ksi
%undefine	with_objc
%endif
%ifarch sparc64
# not bootstrapped yet
%undefine      with_ada
%endif
#
%define		DASHED_SNAP	%{nil}
%define		SNAP		%(echo %{DASHED_SNAP} | sed -e "s#-##g")
%define		GCC_VERSION	3.3.6
%define		KSI_VERSION	1.1.0.1567

Summary:	GNU Compiler Collection: the C compiler and shared files
Summary(es):	Colección de compiladores GNU: el compilador C y ficheros compartidos
Summary(pl):	Kolekcja kompilatorów GNU: kompilator C i pliki wspó³dzielone
Summary(pt_BR):	Coleção dos compiladores GNU: o compilador C e arquivos compartilhados
Name:		gcc
Version:	%{GCC_VERSION}
Release:	3.9
Epoch:		5
License:	GPL v2+
Group:		Development/Languages
Source0:	ftp://gcc.gnu.org/pub/gcc/releases/gcc-%{GCC_VERSION}/%{name}-%{GCC_VERSION}.tar.bz2
# Source0-md5:	6936616a967da5a0b46f1e7424a06414
Source1:	ftp://ftp.pld-linux.org/people/malekith/ksi/ksi-%{KSI_VERSION}.tar.gz
# Source1-md5:	66f07491b44f06928fd95b0e65bb8cd3
Source2:	http://ep09.pld-linux.org/~djrzulf/gcc33/%{name}-non-english-man-pages.tar.bz2
# Source2-md5:	4736f3422ddfb808423b745629acc321
Patch0:		%{name}-info.patch
Patch1:		%{name}-paths.patch
Patch2:		%{name}-nolocalefiles.patch
Patch3:		%{name}-ada-link-new-libgnat.patch
Patch4:		%{name}-nodebug.patch
Patch5:		%{name}-cse-find_best_addr.patch
Patch6:		%{name}-amd64-thunk.patch
Patch7:		%{name}-bug12491.patch
# -- stolen patches from RH --
Patch10:	gcc32-ada-link.patch
Patch11:	gcc32-boehm-gc-libs.patch
Patch12:	gcc32-bogus-inline.patch
Patch13:	gcc32-c++-nrv-test.patch
Patch14:	gcc32-c++-tsubst-asm.patch
Patch15:	gcc32-debug-pr7241.patch
Patch16:	gcc32-duplicate-decl.patch
Patch17:	gcc32-dwarf2-pr6381.patch
Patch18:	gcc32-dwarf2-pr6436-test.patch
Patch19:	gcc32-fde-merge-compat.patch
Patch20:	gcc32-i386-memtest-test.patch
Patch21:	gcc32-inline-label.patch
Patch22:	gcc32-java-no-rpath.patch
Patch23:	gcc32-test-rh65771.patch
Patch24:	gcc32-test-rotate.patch
Patch25:	gcc-cmpi.patch
Patch26:	gcc-ffi64.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	binutils >= 2:2.15.90.0.3
BuildRequires:	bison
%ifarch sparc64
%{?with_boot64:BuildRequires:	crosssparc64-binutils >= 1.15.90.0.3}
%endif
BuildRequires:	fileutils >= 4.0.41
%{?with_ada:%{!?with_bootstrap:BuildRequires:	gcc(ada)}}
%{?with_ada:BuildRequires: gcc-ada}
BuildRequires:	gettext-devel
BuildRequires:	glibc-devel >= 2.2.5-20
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
BuildRequires:	perl-devel
BuildRequires:	texinfo >= 4.1
BuildRequires:	zlib-devel
Requires:	binutils >= 2:2.15.90.0.3
Requires:	gcc-dirs
Requires:	libgcc = %{epoch}:%{GCC_VERSION}-%{release}
%{?with_ada:Provides: gcc(ada)}
Obsoletes:	gcc-chill
Conflicts:	glibc-devel < 2.2.5-20
URL:		http://gcc.gnu.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_slibdir	/%{_lib}
%ifarch %{x8664} ppc64 s390x sparc64
%define		_slibdir32	/lib
%define		_libdir32	/usr/lib
%endif
%ifarch sparc64
# skip -m64, gcc needs to add -m32 for 32-bit libs
%define		rpmcflags	-O2 -mtune=ultrasparc
%endif

%description
A compiler aimed at integrating all the optimizations and features
necessary for a high-performance and stable development environment.

This package contains the C compiler and some files shared by various
parts of the GNU Compiler Collection. In order to use another GCC
compiler you will need to install the appropriate subpackage.

%description -l es
Un compilador destinado a la integración de todas las optimalizaciones
y características necesarias para un entorno de desarrollo eficaz y
estable.

Este paquete contiene el compilador de C y unos ficheros compartidos
por varias parted de la colección de compiladores GNU (GCC). Para usar
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
Version:	%{GCC_VERSION}
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

%package -n libgcc32
Summary:	Shared gcc library - 32 bit version
Summary(es):	Biblioteca compartida de gcc
Summary(pl):	Biblioteka gcc - wersja 32 bitowa
Summary(pt_BR):	Biblioteca runtime para o GCC
Version:	%{GCC_VERSION}
License:	GPL with unlimited link permission
Group:		Libraries

%description -n libgcc32
Shared gcc library - 32 bit version.

%description -n libgcc32 -l es
Biblioteca compartida de gcc.

%description -n libgcc32 -l pl
Biblioteka dynamiczna gcc w wersji 32 bitowej.

%description -n libgcc32 -l pt_BR
Biblioteca runtime para o GCC.

%package c++
Summary:	C++ support for gcc
Summary(es):	Soporte de C++ para gcc
Summary(pl):	Obs³uga C++ dla gcc
Summary(pt_BR):	Suporte C++ para o gcc
Group:		Development/Languages
Requires:	%{name} = %{epoch}:%{GCC_VERSION}-%{release}
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

%package c++32
Summary:	C++ support for gcc - 32 bit version
Summary(es):	Soporte de C++ para gcc
Summary(pl):	Obs³uga C++ dla 32 bitowego gcc
Summary(pt_BR):	Suporte C++ para o gcc
Group:		Development/Languages
Requires:	%{name}-c++ = %{epoch}:%{GCC_VERSION}-%{release}

%description c++32
This package adds C++ support to the GNU Compiler Collection. It
includes support for most of the current C++ specification, including
templates and exception handling. It does not include a standard C++
library, which is available separately.

%description c++32 -l de
Dieses Paket enthält die C++-Unterstützung für den
GNU-Compiler-Collection. Es unterstützt die aktuelle
C++-Spezifikation, inkl. Templates und Ausnahmeverarbeitung. Eine
C++-Standard-Library ist nicht enthalten - sie ist getrennt
erhältlich.

%description c++32 -l es
Este paquete añade soporte de C++ al GCC (colección de compiladores
GNU). Ello incluye el soporte para la mayoría de la especificación
actual de C++, incluyendo plantillas y manejo de excepciones. No
incluye la biblioteca estándar de C++, la que es disponible separada.

%description c++32 -l fr
Ce package ajoute un support C++ a la collection de compilateurs GNU.
Il comprend un support pour la plupart des spécifications actuelles de
C++, dont les modéles et la gestion des exceptions. Il ne comprend pas
une bibliothéque C++ standard, qui est disponible séparément.

%description c++32 -l pl
Ten pakiet dodaje obs³ugê C++ do kompilatora gcc. Ma wsparcie dla
du¿ej ilo¶ci obecnych specyfikacji C++, nie zawiera natomiast
standardowych bibliotek C++, które s± w oddzielnym pakiecie.

%description c++32 -l pt_BR
Este pacote adiciona suporte C++ para o gcc.

%description c++32 -l tr
Bu paket, GNU C derleyicisine C++ desteði ekler. 'Template'ler ve
aykýrý durum iþleme gibi çoðu güncel C++ tanýmlarýna uyar. Standart
C++ kitaplýðý bu pakette yer almaz.

%package objc
Summary:	Objective C support for gcc
Summary(de):	Objektive C-Unterstützung für gcc
Summary(es):	Soporte de Objective C para gcc
Summary(fr):	Gestion d'Objective C pour gcc
Summary(pl):	Obs³uga obiektowego C dla kompilatora gcc
Summary(tr):	gcc için Objective C desteði
Group:		Development/Languages
Requires:	%{name} = %{epoch}:%{GCC_VERSION}-%{release}
Requires:	libobjc = %{epoch}:%{GCC_VERSION}-%{release}
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

%package objc32
Summary:	Objective C support for gcc - 32 bit version
Summary(de):	Objektive C-Unterstützung für gcc
Summary(es):	Soporte de Objective C para gcc
Summary(fr):	Gestion d'Objective C pour gcc
Summary(pl):	Obs³uga obiektowego C dla kompilatora gcc w wersji 32 bitowej
Summary(tr):	gcc için Objective C desteði
Group:		Development/Languages
Requires:	%{name}-objc = %{epoch}:%{GCC_VERSION}-%{release}
Requires:	libobjc32 = %{epoch}:%{GCC_VERSION}-%{release}

%description objc32
This package adds Objective C support to the GNU Compiler Collection.
Objective C is a object oriented derivative of the C language, mainly
used on systems running NeXTSTEP. This package does not include the
standard objective C object library.

%description objc32 -l de
Dieses Paket ergänzt den GNU-Compiler-Collection durch
Objective-C-Support. Objective C ist ein objektorientiertes Derivat
von C, das zur Hauptsache auf Systemen mit NeXTSTEP zum Einsatz kommt.
Die Standard-Objective-C-Objekt-Library ist nicht Teil des Pakets.

%description objc32 -l es
Este paquete añade soporte de Objective C al GCC (colección de
compiladores GNU). Objective C es un lenguaje orientado a objetos
derivado de C, principalmente usado en sistemas que funcionan bajo
NeXTSTEP. El paquete no incluye la biblioteca de objetos estándar de
Objective C.

%description objc32 -l fr
Ce package ajoute un support Objective C a la collection de
compilateurs GNU. L'Objective C est un langage orienté objetdérivé du
langage C, principalement utilisé sur les systèmes NeXTSTEP. Ce
package n'inclue pas la bibliothéque Objective C standard.

%description objc32 -l pl
Ten pakiet dodaje obs³ugê obiektowego C do kompilatora gcc. Obiektowe
C (objc) jest zorientowan± obiektowo pochodn± jêzyka C, u¿ywan±
g³ównie w systemach u¿ywaj±cych NeXTSTEP. W pakiecie nie ma
standardowej biblioteki objc (która znajduje siê w osobnym pakiecie).

%description objc32 -l tr
Bu paket, GNU C derleyicisine Objective C desteði ekler. Objective C,
C dilinin nesne yönelik bir türevidir ve NeXTSTEP altýnda çalýþan
sistemlerde yaygýn olarak kullanýlýr. Standart Objective C nesne
kitaplýðý bu pakette yer almaz.

%package -n libobjc
Summary:	Objective C Libraries
Summary(es):	Bibliotecas de Objective C
Summary(pl):	Biblioteki Obiektowego C
License:	GPL v2+ + linking exception
Version:	%{GCC_VERSION}
Group:		Libraries
Obsoletes:	libobjc1

%description -n libobjc
Objective C Libraries.

%description -n libobjc -l es
Bibliotecas de Objective C.

%description -n libobjc -l pl
Biblioteki Obiektowego C.

%package -n libobjc32
Summary:	Objective C Libraries - 32 bit version
Summary(es):	Bibliotecas de Objective C
Summary(pl):	Biblioteki Obiektowego C w wersji 32 bitowej
License:	GPL v2+ + linking exception
Version:	%{GCC_VERSION}
Group:		Libraries

%description -n libobjc32
Objective C Libraries.

%description -n libobjc32 -l es
Bibliotecas de Objective C.

%description -n libobjc32 -l pl
Biblioteki Obiektowego C.

%package -n libobjc-static
Summary:	Static Objective C Libraries
Summary(es):	Bibliotecas estáticas de Objective C
Summary(pl):	Statyczne Biblioteki Obiektowego C
Version:	%{GCC_VERSION}
License:	GPL v2+ with linking exception
Group:		Development/Libraries
Requires:	libobjc = %{epoch}:%{GCC_VERSION}-%{release}

%description -n libobjc-static
Static Objective C Libraries.

%description -n libobjc-static -l es
Bibliotecas estáticas de Objective C.

%description -n libobjc-static -l pl
Statyczne biblioteki Obiektowego C.

%package -n libobjc32-static
Summary:	Static Objective C Libraries - 32 bit version
Summary(es):	Bibliotecas estáticas de Objective C
Summary(pl):	Statyczne Biblioteki Obiektowego C w wersji 32 bitowej
Version:	%{GCC_VERSION}
License:	GPL v2+ with linking exception
Group:		Development/Libraries
Requires:	libobjc32 = %{epoch}:%{GCC_VERSION}-%{release}

%description -n libobjc32-static
Static Objective C Libraries.

%description -n libobjc32-static -l es
Bibliotecas estáticas de Objective C.

%description -n libobjc32-static -l pl
Statyczne biblioteki Obiektowego C.

%package g77
Summary:	Fortran 77 support for gcc
Summary(es):	Soporte de Fortran 77 para gcc
Summary(pl):	Obs³uga Fortranu 77 dla gcc
Summary(pt_BR):	Suporte Fortran 77 para o GCC
Version:	%{GCC_VERSION}
Group:		Development/Languages/Fortran
Requires:	%{name} = %{epoch}:%{GCC_VERSION}-%{release}
Requires:	libg2c = %{epoch}:%{GCC_VERSION}-%{release}
Obsoletes:	egcs-g77

%description g77
This package adds support for compiling Fortran 77 programs with the
GNU compiler.

%description g77 -l es
Este paquete añade soporte para compilar programas escritos en Fortran
77 con el compilador GNU.

%description g77 -l pl
Ten pakiet dodaje obs³ugê Fortranu 77 do kompilatora gcc. Jest
potrzebny do kompilowania programów pisanych w jêzyku Fortran 77.

%description g77 -l pt_BR
Suporte Fortran 77 para o GCC.

%package g7732
Summary:	Fortran 77 support for gcc - 32 bit version
Summary(es):	Soporte de Fortran 77 para gcc
Summary(pl):	Obs³uga Fortranu 77 dla gcc w wersji 32 bitowej
Summary(pt_BR):	Suporte Fortran 77 para o GCC
Version:	%{GCC_VERSION}
Group:		Development/Languages/Fortran
Requires:	%{name}-g77 = %{epoch}:%{GCC_VERSION}-%{release}
Requires:	libg2c32 = %{epoch}:%{GCC_VERSION}-%{release}

%description g7732
This package adds support for compiling Fortran 77 programs with the
GNU compiler.

%description g7732 -l es
Este paquete añade soporte para compilar programas escritos en Fortran
77 con el compilador GNU.

%description g7732 -l pl
Ten pakiet dodaje obs³ugê Fortranu 77 do kompilatora gcc. Jest
potrzebny do kompilowania programów pisanych w jêzyku Fortran 77.

%description g7732 -l pt_BR
Suporte Fortran 77 para o GCC.

%package -n libg2c
Summary:	Fortran 77 Libraries
Summary(es):	Bibliotecas de Fortran 77
Summary(pl):	Biblioteki Fortranu 77
Version:	%{GCC_VERSION}
License:	LGPL v2+
Group:		Libraries

%description -n libg2c
Fortran 77 Libraries.

%description -n libg2c -l es
Bibliotecas de Fortran 77.

%description -n libg2c -l pl
Biblioteki Fortranu 77.

%package -n libg2c32
Summary:	Fortran 77 Libraries - 32 bit version
Summary(es):	Bibliotecas de Fortran 77
Summary(pl):	Biblioteki Fortranu 77 w wersji 32 bitowej
Version:	%{GCC_VERSION}
License:	LGPL v2+
Group:		Libraries

%description -n libg2c32
Fortran 77 Libraries.

%description -n libg2c32 -l es
Bibliotecas de Fortran 77.

%description -n libg2c32 -l pl
Biblioteki Fortranu 77.

%package -n libg2c-static
Summary:	Static Fortran 77 Libraries
Summary(es):	Bibliotecas estáticas de Fortran 77
Summary(pl):	Statyczne Biblioteki Fortranu 77
Version:	%{GCC_VERSION}
License:	LGPL v2+
Group:		Development/Libraries
Requires:	libg2c = %{epoch}:%{GCC_VERSION}-%{release}

%description -n libg2c-static
Static Fortran 77 Libraries.

%description -n libg2c-static -l es
Bibliotecas estáticas de Fortran 77.

%description -n libg2c-static -l pl
Statyczne biblioteki Fortranu 77.

%package -n libg2c32-static
Summary:	Static Fortran 77 Libraries - 32 bit version
Summary(es):	Bibliotecas estáticas de Fortran 77
Summary(pl):	Statyczne Biblioteki Fortranu 77 w wersji 32 bitowej
Version:	%{GCC_VERSION}
License:	LGPL v2+
Group:		Development/Libraries
Requires:	libg2c32 = %{epoch}:%{GCC_VERSION}-%{release}

%description -n libg2c32-static
Static Fortran 77 Libraries.

%description -n libg2c32-static -l es
Bibliotecas estáticas de Fortran 77.

%description -n libg2c32-static -l pl
Statyczne biblioteki Fortranu 77.

%package java
Summary:	Java support for gcc
Summary(es):	Soporte de Java para gcc
Summary(pl):	Obs³uga Javy dla gcc
Version:	%{GCC_VERSION}
Group:		Development/Languages/Java
Requires:	%{name} = %{epoch}:%{GCC_VERSION}-%{release}
Requires:	libgcj-devel = %{epoch}:%{GCC_VERSION}-%{release}
Requires:	java-shared
Provides:	gcj = %{epoch}:%{GCC_VERSION}-%{release}

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

%package java-tools
Summary:	Shared java tools
Summary(es):	Herramientas compartidas de Java
Summary(pl):	Wspó³dzielone narzêdzia javy
Version:	%{GCC_VERSION}
Group:		Development/Languages/Java
Provides:	jar = %{epoch}:%{GCC_VERSION}-%{release}
Provides:	java-shared
Obsoletes:	fastjar
Obsoletes:	jar
Obsoletes:	java-shared

%description java-tools
This package contains tools that are common for every Java(tm)
implementation, such as rmic or jar.

%description java-tools -l es
Este paquete contiene herramientas que son comunes para cada
implementación de Java(tm), como rmic o jar.

%description java-tools -l pl
Pakiet ten zawiera narzêdzia wspólne dla ka¿dej implementacji
Javy(tm), takie jak rmic czy jar.

%package -n libgcj
Summary:	Java Class Libraries
Summary(es):	Bibliotecas de clases de Java
Summary(pl):	Biblioteki Klas Javy
Version:	%{GCC_VERSION}
License:	GPL with limited linking exception
Group:		Libraries
Obsoletes:	libgcj3

%description -n libgcj
Java Class Libraries.

%description -n libgcj -l es
Bibliotecas de clases de Java.

%description -n libgcj -l pl
Biblioteki Klas Javy.

%package -n libgcj32
Summary:	Java Class Libraries - 32 bit version
Summary(es):	Bibliotecas de clases de Java
Summary(pl):	Biblioteki Klas Javy w wersji 32 bitowej
Version:	%{GCC_VERSION}
License:	GPL with limited linking exception
Group:		Libraries

%description -n libgcj32
Java Class Libraries.

%description -n libgcj32 -l es
Bibliotecas de clases de Java.

%description -n libgcj32 -l pl
Biblioteki Klas Javy.

%package -n libgcj-devel
Summary:	Development files for Java Class Libraries
Summary(es):	Ficheros de desarrollo para las bibliotecas de clases de Java
Summary(pl):	Pliki nag³ówkowe dla Bibliotek Klas Javy
Version:	%{GCC_VERSION}
License:	GPL with limited linking exception
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{GCC_VERSION}-%{release}
Requires:	libgcj = %{epoch}:%{GCC_VERSION}-%{release}
Requires:	zlib-devel
Obsoletes:	libgcj3-devel

%description -n libgcj-devel
Development files for Java Class Libraries.

%description -n libgcj-devel -l es
Ficheros de desarrollo para las bibliotecas de clases de Java.

%description -n libgcj-devel -l pl
Pliki nag³ówkowe dla Bibliotek Klas Javy.

%package -n libgcj32-devel
Summary:	Development files for Java Class Libraries - 32 bit version
Summary(es):	Ficheros de desarrollo para las bibliotecas de clases de Java
Summary(pl):	Pliki nag³ówkowe dla Bibliotek Klas Javy w wersji 32 bitowej
Version:	%{GCC_VERSION}
License:	GPL with limited linking exception
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{GCC_VERSION}-%{release}
Requires:	libgcj32 = %{epoch}:%{GCC_VERSION}-%{release}
Requires:	zlib-devel

%description -n libgcj32-devel
Development files for Java Class Libraries.

%description -n libgcj32-devel -l es
Ficheros de desarrollo para las bibliotecas de clases de Java.

%description -n libgcj32-devel -l pl
Pliki nag³ówkowe dla Bibliotek Klas Javy.

%package -n libgcj-static
Summary:	Static Java Class Libraries
Summary(es):	Bibliotecas estáticas de clases de Java
Summary(pl):	Statyczne Biblioteki Klas Javy
Version:	%{GCC_VERSION}
License:	GPL with limited linking exception
Group:		Development/Libraries
Requires:	libgcj-devel = %{epoch}:%{GCC_VERSION}-%{release}
Requires:	libstdc++-devel = %{epoch}:%{GCC_VERSION}-%{release}

%description -n libgcj-static
Static Java Class Libraries.

%description -n libgcj-static -l es
Bibliotecas estáticas de clases de Java.

%description -n libgcj-static -l pl
Statyczne Biblioteki Klas Javy.

%package -n libgcj32-static
Summary:	Static Java Class Libraries - 32 bit version
Summary(es):	Bibliotecas estáticas de clases de Java
Summary(pl):	Statyczne Biblioteki Klas Javy w wersji 32 bitowej
Version:	%{GCC_VERSION}
License:	GPL with limited linking exception
Group:		Development/Libraries
Requires:	libgcj32-devel = %{epoch}:%{GCC_VERSION}-%{release}
Requires:	libstdc++32-devel = %{epoch}:%{GCC_VERSION}-%{release}

%description -n libgcj32-static
Static Java Class Libraries.

%description -n libgcj32-static -l es
Bibliotecas estáticas de clases de Java.

%description -n libgcj32-static -l pl
Statyczne Biblioteki Klas Javy.

%package -n libstdc++
Summary:	GNU C++ library
Summary(es):	Biblioteca C++ de GNU
Summary(pl):	Biblioteki GNU C++
Summary(pt_BR):	Biblioteca C++ GNU
Version:	%{GCC_VERSION}
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

%package -n libstdc++32
Summary:	GNU C++ library - 32 bit version
Summary(es):	Biblioteca C++ de GNU
Summary(pl):	Biblioteki GNU C++ w wersji 32 bitowej
Summary(pt_BR):	Biblioteca C++ GNU
Version:	%{GCC_VERSION}
License:	GPL v2+ with free software exception
Group:		Libraries

%description -n libstdc++32
This is the GNU implementation of the standard C++ libraries, along
with additional GNU tools. This package includes the shared libraries
necessary to run C++ applications.

%description -n libstdc++32 -l de
Dies ist die GNU-Implementierung der Standard-C++-Libraries mit
weiteren GNU-Tools. Dieses Paket enthält die zum Ausführen von
C++-Anwendungen erforderlichen gemeinsam genutzten Libraries.

%description -n libstdc++32 -l es
Este es el soporte de las bibliotecas padrón del C++, junto con
herramientas GNU adicionales. El paquete incluye las bibliotecas
compartidas necesarias para ejecutar aplicaciones C++.

%description -n libstdc++32 -l fr
Ceci est l'implémentation GNU des librairies C++ standard, ainsi que
des outils GNU supplémentaires. Ce package comprend les librairies
partagées nécessaires à l'exécution d'application C++.

%description -n libstdc++32 -l pl
Pakiet ten zawiera biblioteki bêd±ce implementacj± standardowych
bibliotek C++. Znajduj± siê w nim biblioteki dynamiczne niezbêdne do
uruchomienia aplikacji napisanych w C++.

%description -n libstdc++32 -l pt_BR
Este pacote é uma implementação da biblioteca padrão C++ v3, um
subconjunto do padrão ISO 14882.

%description -n libstdc++32 -l tr
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
Version:	%{GCC_VERSION}
License:	GPL v2+ with free software exception
Group:		Development/Libraries
Requires:	%{name}-c++ = %{epoch}:%{GCC_VERSION}-%{release}
Requires:	libstdc++ = %{epoch}:%{GCC_VERSION}-%{release}
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

%package -n libstdc++32-devel
Summary:	Header files and documentation for C++ development
Summary(de):	Header-Dateien zur Entwicklung mit C++
Summary(es):	Ficheros de cabecera y documentación para desarrollo C++
Summary(fr):	Fichiers d'en-tête et biblitothèques pour développer en C++
Summary(pl):	Pliki nag³ówkowe i dokumentacja do biblioteki standardowej C++
Summary(pt_BR):	Arquivos de inclusão e bibliotecas para o desenvolvimento em C++
Summary(tr):	C++ ile program geliþtirmek için gerekli dosyalar
Version:	%{GCC_VERSION}
License:	GPL v2+ with free software exception
Group:		Development/Libraries
Requires:	%{name}-c++32 = %{epoch}:%{GCC_VERSION}-%{release}
Requires:	libstdc++32 = %{epoch}:%{GCC_VERSION}-%{release}
Requires:	glibc-devel

%description -n libstdc++32-devel
This is the GNU implementation of the standard C++ libraries. This
package includes the header files needed for C++ development and
library documentation.

%description -n libstdc++32-devel -l es
Este es el soporte de las bibliotecas padrón del lenguaje C++. Este
paquete incluye los archivos de inclusión y bibliotecas necesarios
para desarrollo de programas en lenguaje C++.

%description -n libstdc++32-devel -l pl
Pakiet ten zawiera biblioteki bêd±ce implementacj± standardowych
bibliotek C++. Znajduj± siê w nim pliki nag³ówkowe wykorzystywane przy
programowaniu w jêzyku C++ oraz dokumentacja biblioteki standardowej.

%description -n libstdc++32-devel -l pt_BR
Este pacote inclui os arquivos de inclusão e bibliotecas necessárias
para desenvolvimento de programas C++.

%package -n libstdc++-static
Summary:	Static C++ standard library
Summary(es):	Biblioteca estándar estática de C++
Summary(pl):	Statyczna biblioteka standardowa C++
Version:	%{GCC_VERSION}
License:	GPL v2+ with free software exception
Group:		Development/Libraries
Requires:	libstdc++-devel = %{epoch}:%{GCC_VERSION}-%{release}

%description -n libstdc++-static
Static C++ standard library.

%description -n libstdc++-static -l es
Biblioteca estándar estática de C++.

%description -n libstdc++-static -l pl
Statyczna biblioteka standardowa C++.

%package -n libstdc++32-static
Summary:	Static C++ standard library - 32 bit version
Summary(es):	Biblioteca estándar estática de C++
Summary(pl):	Statyczna biblioteka standardowa C++ w wersji 32 bitowej
Version:	%{GCC_VERSION}
License:	GPL v2+ with free software exception
Group:		Development/Libraries
Requires:	libstdc++32-devel = %{epoch}:%{GCC_VERSION}-%{release}

%description -n libstdc++32-static
Static C++ standard library.

%description -n libstdc++32-static -l es
Biblioteca estándar estática de C++.

%description -n libstdc++32-static -l pl
Statyczna biblioteka standardowa C++.

%package -n libffi
Summary:	Foreign Function Interface library
Summary(es):	Biblioteca de interfaz de funciones ajenas
Summary(pl):	Biblioteka zewnêtrznych wywo³añ funkcji
Version:	%{GCC_VERSION}
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

%package -n libffi32
Summary:	Foreign Function Interface library - 32 bit version
Summary(es):	Biblioteca de interfaz de funciones ajenas
Summary(pl):	Biblioteka zewnêtrznych wywo³añ funkcji w wersji 32 bitowej
Version:	%{GCC_VERSION}
License:	BSD-like
Group:		Libraries

%description -n libffi32
The libffi library provides a portable, high level programming
interface to various calling conventions. This allows a programmer to
call any function specified by a call interface description at run
time.

%description -n libffi32 -l es
La biblioteca libffi provee una interfaz portable de programación de
alto nivel para varias convenciones de llamada. Ello permite que un
programador llame una función cualquiera especificada por una
descripción de interfaz de llamada en el tiempo de ejecución.

%description -n libffi32 -l pl
Biblioteka libffi dostarcza przeno¶nego, wysokopoziomowego
miêdzymordzia do ró¿nych konwencji wywo³añ funkcji. Pozwala to
programi¶cie wywo³ywaæ dowolne funkcje podaj±c konwencjê wywo³ania w
czasie wykonania.

%package -n libffi-devel
Summary:	Development files for Foreign Function Interface library
Summary(es):	Ficheros de desarrollo para libffi
Summary(pl):	Pliki nag³ówkowe dla libffi
Version:	%{GCC_VERSION}
License:	BSD-like
Group:		Development/Libraries
Requires:	libffi = %{epoch}:%{GCC_VERSION}-%{release}

%description -n libffi-devel
Development files for Foreign Function Interface library.

%description -n libffi-devel -l es
Ficheros de desarrollo para libffi.

%description -n libffi-devel -l pl
Pliki nag³ówkowe dla libffi.

%package -n libffi32-devel
Summary:	Development files for Foreign Function Interface library - 32 bit version
Summary(es):	Ficheros de desarrollo para libffi
Summary(pl):	Pliki nag³ówkowe dla libffi w wersji 32 bitowej
Version:	%{GCC_VERSION}
License:	BSD-like
Group:		Development/Libraries
Requires:	libffi32 = %{epoch}:%{GCC_VERSION}-%{release}

%description -n libffi32-devel
Development files for Foreign Function Interface library.

%description -n libffi32-devel -l es
Ficheros de desarrollo para libffi.

%description -n libffi32-devel -l pl
Pliki nag³ówkowe dla libffi.

%package -n libffi-static
Summary:	Static Foreign Function Interface library
Summary(es):	Biblioteca libffi estática
Summary(pl):	Statyczna biblioteka libffi
Version:	%{GCC_VERSION}
License:	BSD-like
Group:		Development/Libraries
Requires:	libffi-devel = %{epoch}:%{GCC_VERSION}-%{release}

%description -n libffi-static
Static Foreign Function Interface library.

%description -n libffi-static -l es
Biblioteca libffi estática.

%description -n libffi-static -l pl
Statyczna biblioteka libffi.

%package -n libffi32-static
Summary:	Static Foreign Function Interface library - 32 bit version
Summary(es):	Biblioteca libffi estática
Summary(pl):	Statyczna biblioteka libffi w wersji 32 bitowej
Version:	%{GCC_VERSION}
License:	BSD-like
Group:		Development/Libraries
Requires:	libffi32-devel = %{epoch}:%{GCC_VERSION}-%{release}

%description -n libffi32-static
Static Foreign Function Interface library.

%description -n libffi32-static -l es
Biblioteca libffi estática.

%description -n libffi32-static -l pl
Statyczna biblioteka libffi.

%package ada
Summary:	Ada support for gcc
Summary(es):	Soporte de Ada para gcc
Summary(pl):	Obs³uga Ady do gcc
Version:	%{GCC_VERSION}
Group:		Development/Languages
Requires:	%{name} = %{epoch}:%{GCC_VERSION}-%{release}
Requires:	libgnat = %{epoch}:%{GCC_VERSION}-%{release}
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
Version:	%{GCC_VERSION}
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
Version:	%{GCC_VERSION}
License:	GPL v2+ with linking exception
Group:		Development/Libraries
Obsoletes:	gnat-static

%description -n libgnat-static
This package contains static libraries for programs written in Ada.

%description -n libgnat-static -l pl
Ten pakiet zawiera biblioteki statyczne dla programów napisanych w
Adzie.

%package ksi
Summary:	Ksi support for gcc
Summary(es):	Soporte de Ksi para gcc
Summary(pl):	Obs³uga Ksi dla gcc
Version:	%{GCC_VERSION}.%{KSI_VERSION}
Group:		Development/Languages
Requires:	%{name} = %{epoch}:%{GCC_VERSION}-%{release}

%description ksi
This package adds experimental support for compiling Ksi programs into
native code. You proabably don't need it, unless your are going to
develop a compiler using Ksi as intermediate representation or you are
using such compiler (like Gont).

%description ksi -l es
Este paquete añade soporte experimental para compilar programas de Ksi
en código nativo. Probablemento no lo necesitará, a menos que vaya a
desarrollar un compilador que use Ksi como representación intermedia o
use tal compilador (como Gont).

%description ksi -l pl
Ten pakiet dodaje eksperymentalne wsparcie dla kompilacji programów w
Ksi do kodu maszynowego. Prawdopodobnie nie potrzebujesz go, chyba ¿e
zamierzasz pisaæ kompilator u¿ywaj±cy Ksi jako reprezentacji
po¶rednicz±cej, lub u¿ywasz takiego kompilatora (jak Gont).

%package -n cpp
Summary:	The C Pre Processor
Summary(es):	El preprocesador de C
Summary(pl):	Preprocesor C
Summary(pt_BR):	Preprocessador para a linguagem C
Version:	%{GCC_VERSION}
Group:		Development/Languages
# uses cc1 (or cc1plus if -x c++) backend
Requires:	%{name} = %{epoch}:%{GCC_VERSION}-%{release}
Obsoletes:	egcs-cpp
Obsoletes:	gcc-cpp
Obsoletes:	gpp

%description -n cpp
The C preprocessor is a "macro processor" that is used automatically
by the C compiler to transform your program before actual compilation.
It is called a macro processor because it allows you to define
"macros", which are brief abbreviations for longer constructs.

The C preprocessor provides four separate facilities that you can use
as you see fit:

- Inclusion of header files. These are files of declarations that can
  be substituted into your program.
- Macro expansion. You can define "macros", which are abbreviations
  for arbitrary fragments of C code, and then the C preprocessor will
  replace the macros with their definitions throughout the program.
- Conditional compilation. Using special preprocessing directives, you
  can include or exclude parts of the program according to various
  conditions.
- Line control. If you use a program to combine or rearrange source
  files into an intermediate file which is then compiled, you can use
  line control to inform the compiler of where each source line
  originally came from.

%description -n cpp -l es
El preprocesador de C es un "procesador de macros" que es usado
automáticamente por el compilador C para transformar su programa antes
de que éste se actualmente compile. Se llama procesador de macros
porque permite definir "macros", los que son abreviaciones concisas
para construcciones más largas.

El preprocesador C provee cuatro cualidadedes distintas que puede usar
como le convenga:

- Inclusión de ficheros de cabecera. Éstos son ficheros de
  declaraciones que pueden incorporarse a su programa.
- Expansión de macros. Puede definir "macros", los que son
  abreviaciones para fragmentos arbitrarios de código C, y a lo largo
  del programa el preprocesador sustituirá los macros con sus
  definiciones.
- Compilación condicional. Usando especiales directivas del preproceso
  puede incluir o excluir partes del programa según varias condiciones.
- Control de líneas. Si usa un programa para combinar o reorganizar el
  código fuente en un fichero intermedio que luego es compilado, puede
  usar control de líneas para informar el compilador de dónde origina
  cada línea.

%description -n cpp -l pl
Preprocesor C jest "makro procesorem" który jest automatycznie
u¿ywany przez kompilator C do obróbki kompilowanego programu przed
w³a¶ciw± kompilacj±. Jest on nazywany makroprocesorem, poniewa¿
umo¿liwia definiowanie i rozwijanie makr umo¿liwiaj±cych skracanie
d³ugich konstrukcji w jêzyku C.

Preprocesor C umo¿liwia wykonywanie czterech ró¿nych typów operacji:

- Do³±czanie plików (np. nag³ówkowych). Wstawia pliki w miejscu
  deklaracji polecenia do³±czenia innego pliku.
- Rozwijanie makr. Mo¿na definiowaæ "makra" nadaj±c im identyfikatory,
  których pó¼niejsze u¿ycie powoduje podczas rozwijania podmienienie
  indentyfikatora deklarowan± wcze¶niej warto¶ci±.
- Kompilacja warunkowa. W zale¿no¶ci od obecno¶ci symboli i dyrektyw w
  ¶rodowisku preprocesora s± w³±czane warunkowo, b±d¼ nie, pewne
  fragmenty obrabianego strumienia tekstów.
- Kontrola linii ¼ród³a. Niezale¿nie od tego jakim przeobra¿eniom
  podlega wynikowy strumieñ danych w wyniku rozwijania makr i do³±czania
  s± zapamiêtywane informacje o tym, której linii pliku ¼ród³owego
  odpowiada fragment pliku wynikowego.

%description -n cpp -l pt_BR
O preprocessador C é um "processador de macros", que é utilizado pelo
compilador C para fazer algumas modificações no seu programa, antes da
compilação em si. Ele é chamado de "processador de macros" porque
permite a você definir "macros", que são abreviações para construções
mais complicadas.

O preprocessador C fornece quatro funcionalidades básicas: inclusão de
arquivos de cabeçalho; expansão de macros; compilação condicional; e
controle da numeração das linhas do programa.

%prep
%setup -q -a1 -n %{name}-%{GCC_VERSION}
mv ksi-%{KSI_VERSION} gcc/ksi

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%{!?debug:%patch4 -p1}
%patch5 -p1
%patch6 -p1
%patch7 -p1

%patch10 -p1
%patch11
%patch12
%patch13
%patch14
%patch15

%patch16
%patch17
%patch18
%patch19
%patch20
%patch21
%patch22
%patch23
%patch24
%patch25 -p1
%patch26 -p2

# because we distribute modified version of gcc...
perl -pi -e 's/(version.*)";/$1 (PLD Linux)";/' gcc/version.c
perl -pi -e 's@(bug_report_url.*<URL:).*";@$1http://bugs.pld-linux.org/>";@' gcc/version.c

%build
# cd gcc && autoconf; cd ..
# autoconf is not needed!
cp /usr/share/automake/config.sub .

rm -rf obj-%{_target_platform} && install -d obj-%{_target_platform} && cd obj-%{_target_platform}

# NOTE: enable-symvers is a hack to enforce versioned symbols in (multilib)
# 32-bit libstdc++ (to workaround broken -lgcc_s(_32) check in configure)
CFLAGS="%{rpmcflags}" \
CXXFLAGS="%{rpmcflags}" \
TEXCONFIG=false \
../configure \
	--prefix=%{_prefix} \
	--libdir=%{_libdir} \
	--libexecdir=%{_libdir} \
	--infodir=%{_infodir} \
	--mandir=%{_mandir} \
	--enable-shared \
	--enable-symvers=gnu \
	--enable-threads=posix \
	--enable-__cxa_atexit \
	--enable-languages="c%{?with_cxx:,c++}%{?with_fortran:,f77}%{?with_objc:,objc}%{?with_ada:,ada}%{?with_java:,java}%{?with_ksi:,ksi}" \
	--enable-c99 \
	--enable-long-long \
%ifnarch ppc
%if %{without multilib}
	--disable-multilib \
%endif
%endif
	--enable-nls \
%ifarch sparc64
	--with-cpu=ultrasparc \
%endif
	--with-gnu-as \
	--with-gnu-ld \
	--with-system-zlib \
	--with-slibdir=%{_slibdir} \
	--without-x \
%if %{with boot64}
	--with-as=/usr/bin/as \
	--with-ld=/usr/bin/ld \
	--with-sysroot= \
	--target=%{_target_platform} \
	--host=%{_host_alias} \
	--build=%{_host_alias}
%else
	%{_target_platform}
%endif

PATH=$PATH:/sbin:%{_sbindir}

cd ..
%{__make} -C obj-%{_target_platform} %{?with_boot64:all-gcc}%{!?with_boot64:bootstrap-lean} \
	GCJFLAGS="%{rpmcflags}" \
	LDFLAGS_FOR_TARGET="%{rpmldflags}" \
	mandir=%{_mandir} \
	infodir=%{_infodir}

%if %{with ada}
for tgt in gnatlib gnattools gnatlib-shared; do
%{__make} -C obj-%{_target_platform}/gcc $tgt \
	LDFLAGS_FOR_TARGET="%{rpmldflags}" \
	mandir=%{_mandir} \
	infodir=%{_infodir}
done
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/lib,%{_datadir},%{_infodir}}

cd obj-%{_target_platform}
PATH=$PATH:/sbin:%{_sbindir}

%{__make} install \
	mandir=%{_mandir} \
	infodir=%{_infodir} \
	DESTDIR=$RPM_BUILD_ROOT

%ifarch sparc64
%if %{with boot64}
ln -f $RPM_BUILD_ROOT%{_bindir}/{sparc64-pld-linux-,}gcc
mv -f $RPM_BUILD_ROOT%{_bindir}/{sparc64-pld-linux-,}gccbug
mv -f $RPM_BUILD_ROOT%{_bindir}/{sparc64-pld-linux-,}gcov
mv -f $RPM_BUILD_ROOT%{_bindir}/{sparc64-pld-linux-,}cpp
mv -f $RPM_BUILD_ROOT%{_mandir}/man1/{sparc64-pld-linux-,}gcc.1
%endif
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

ln -sf gcc $RPM_BUILD_ROOT%{_bindir}/cc
echo ".so gcc.1" > $RPM_BUILD_ROOT%{_mandir}/man1/cc.1

%if %{with fortran}
ln -sf g77 $RPM_BUILD_ROOT%{_bindir}/f77
echo ".so g77.1" > $RPM_BUILD_ROOT%{_mandir}/man1/f77.1
%endif

%if %{with ada}
# move ada shared libraries to proper place...
mv $RPM_BUILD_ROOT%{_libdir}/gcc-lib/*/*/adalib/*.so.1 \
	$RPM_BUILD_ROOT%{_libdir}
# check if symlink to be made is valid
test -f $RPM_BUILD_ROOT%{_libdir}/libgnat-3.15.so.1
ln -sf libgnat-3.15.so.1 $RPM_BUILD_ROOT%{_libdir}/libgnat-3.15.so
ln -sf libgnarl-3.15.so.1 $RPM_BUILD_ROOT%{_libdir}/libgnarl-3.15.so
ln -sf libgnat-3.15.so $RPM_BUILD_ROOT%{_libdir}/libgnat.so
ln -sf libgnarl-3.15.so $RPM_BUILD_ROOT%{_libdir}/libgnarl.so
%endif

ln -sf %{_bindir}/cpp $RPM_BUILD_ROOT/lib/cpp

cd ..

%if %{with java}
install -d java-doc
cp -f libjava/doc/cni.sgml libjava/READ* java-doc
cp -f fastjar/README java-doc/README.fastjar
cp -f libffi/README java-doc/README.libffi
cp -f libffi/LICENSE java-doc/LICENSE.libffi
%endif

%if %{with objc}
cp -f libobjc/README gcc/objc/README.libobjc
%endif

# avoid -L poisoning in *.la - there should be only -L%{_libdir}/gcc-lib/*/%{version}
for f in %{?with_cxx:libstdc++.la libsupc++.la} %{?with_java:libgcj.la} ; do
	perl -pi -e 's@-L[^ ]*[acs.] @@g' $RPM_BUILD_ROOT%{_libdir}/$f
done
# normalize libdir, to avoid propagation of unnecessary RPATHs by libtool
for f in \
	%{?with_cxx:libstdc++.la libsupc++.la} \
	%{?with_fortran:libg2c.la} \
	%{?with_java:libgcj.la lib-org-w3c-dom.la lib-org-xml-sax.la libffi.la} \
	%{?with_objc:libobjc.la}; do
	perl -pi -e "s@^libdir='.*@libdir='/usr/%{_lib}'@" $RPM_BUILD_ROOT%{_libdir}/$f
done

bzip2 -dc %{SOURCE2} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}
mv -f $RPM_BUILD_ROOT%{_mandir}/ja/man1/{cccp,cpp}.1

# include/ contains install-tools/include/* and headers that were fixed up
# by fixincludes, we don't want former
gccdir=$(echo $RPM_BUILD_ROOT%{_libdir}/gcc-lib/*/*/)
mkdir $gccdir/tmp
# we have to save these however
for f in syslimits.h %{?with_fortran:g2c.h} %{?with_java:gcj} %{?with_objc:objc} ; do
	mv -f $gccdir/include/$f $gccdir/tmp
done
rm -rf $gccdir/include
mv -f $gccdir/tmp $gccdir/include
cp $gccdir/install-tools/include/*.h $gccdir/include
# but we don't want anything more from install-tools
rm -rf $gccdir/install-tools

%if %{with multilib}
ln -sf %{_slibdir}/libgcc_s.so.1 $gccdir/libgcc_s.so
ln -sf %{_slibdir32}/libgcc_s.so.1 $gccdir/libgcc_s_32.so

%if %{with cxx}
spath=obj-%{_target_platform}/%{_target_platform}
sfile=libstdc++-v3/include/%{_target_platform}/bits/c++config.h
dpath=$RPM_BUILD_ROOT%{_includedir}/c++/%{GCC_VERSION}/%{_target_platform}/bits
if ! cmp $spath/$sfile $spath/32/$sfile > /dev/null ; then
	cp -f $spath/$sfile $dpath/c++config64.h
	cp -f $spath/32/$sfile $dpath/c++config32.h
	cat > $dpath/c++config.h <<EOF
#include <bits/wordsize.h>
#if __WORDSIZE == 32
#include <bits/c++config32.h>
#else
#include <bits/c++config64.h>
#endif
EOF
fi
%endif
%endif

%find_lang %{name}
%if %{with cxx}
%find_lang libstdc\+\+
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%post g77
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun g77
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%post java
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun java
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%post ksi
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun ksi
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%post -n cpp
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun -n cpp
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%post   -p /sbin/ldconfig -n libgcc
%postun -p /sbin/ldconfig -n libgcc
%post   -p /sbin/ldconfig -n libgcc32
%postun -p /sbin/ldconfig -n libgcc32
%post   -p /sbin/ldconfig -n libstdc++
%postun -p /sbin/ldconfig -n libstdc++
%post   -p /sbin/ldconfig -n libstdc++32
%postun -p /sbin/ldconfig -n libstdc++32
%post   -p /sbin/ldconfig -n libobjc
%postun -p /sbin/ldconfig -n libobjc
%post   -p /sbin/ldconfig -n libobjc32
%postun -p /sbin/ldconfig -n libobjc32
%post   -p /sbin/ldconfig -n libg2c
%postun -p /sbin/ldconfig -n libg2c
%post   -p /sbin/ldconfig -n libg2c32
%postun -p /sbin/ldconfig -n libg2c32
%post   -p /sbin/ldconfig -n libgcj
%postun -p /sbin/ldconfig -n libgcj
%post   -p /sbin/ldconfig -n libgcj32
%postun -p /sbin/ldconfig -n libgcj32
%post   -p /sbin/ldconfig -n libgnat
%postun -p /sbin/ldconfig -n libgnat
%post   -p /sbin/ldconfig -n libffi
%postun -p /sbin/ldconfig -n libffi
%post   -p /sbin/ldconfig -n libffi32
%postun -p /sbin/ldconfig -n libffi32

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc READ* ChangeLog
%dir %{_libdir}/gcc-lib/*/*
%dir %{_libdir}/gcc-lib/*/*/include
%attr(755,root,root) %{_bindir}/*-gcc*
%attr(755,root,root) %{_bindir}/gcc
%attr(755,root,root) %{_bindir}/gccbug
%attr(755,root,root) %{_bindir}/gcov
%attr(755,root,root) %{_bindir}/cc

%{_mandir}/man1/gcc.1*
%{_mandir}/man1/cc.1*
%{_mandir}/man1/gcov.1*
%lang(fr) %{_mandir}/fr/man1/gcc.1*
%lang(ja) %{_mandir}/ja/man1/gcc.1*
%{_infodir}/gcc*

%attr(755,root,root) %{_slibdir}/lib*.so
%{_libdir}/gcc-lib/*/*/libgcc.a
%{_libdir}/gcc-lib/*/*/libgcc_eh.a
%{_libdir}/gcc-lib/*/*/specs
%{_libdir}/gcc-lib/*/*/crt*.o
%if %{with multilib}
%attr(755,root,root) %{_libdir}/gcc-lib/*/*/libgcc_s*.so
%dir %{_libdir}/gcc-lib/*/*/32
%{_libdir}/gcc-lib/*/*/32/libgcc.a
%{_libdir}/gcc-lib/*/*/32/libgcc_eh.a
%{_libdir}/gcc-lib/*/*/32/crt*.o
%endif
%ifarch ppc
%{_libdir}/gcc-lib/*/*/ecrt*.o
%{_libdir}/gcc-lib/*/*/ncrt*.o
%{_libdir}/gcc-lib/*/*/nof
%dir %{_libdir}/nof
%endif
%attr(755,root,root) %{_libdir}/gcc-lib/*/*/cc1
%attr(755,root,root) %{_libdir}/gcc-lib/*/*/collect2

%{_libdir}/gcc-lib/*/*/include/*.h
%{?with_fortran:%exclude %{_libdir}/gcc-lib/*/*/include/g2c.h}

%files -n libgcc
%defattr(644,root,root,755)
%attr(755,root,root) %{_slibdir}/lib*.so.*

%if %{with multilib}
%files -n libgcc32
%defattr(644,root,root,755)
%attr(755,root,root) %{_slibdir32}/lib*.so.*
#%attr(755,root,root) %{_libdir}/gcc-lib/*/*/libgcc*.so
%endif

%if %{with cxx}
%files c++
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/g++
%attr(755,root,root) %{_bindir}/*-g++
%attr(755,root,root) %{_bindir}/c++
%attr(755,root,root) %{_bindir}/*-c++
%attr(755,root,root) %{_libdir}/gcc-lib/*/*/cc1plus
%{_libdir}/libsupc++.la
%{_libdir}/libsupc++.a
%ifarch ppc
%{_libdir}/nof/libsupc++.la
%{_libdir}/nof/libsupc++.a
%endif
%{_mandir}/man1/g++.1*
%lang(ja) %{_mandir}/ja/man1/g++.1*

%if %{with multilib}
%files c++32
%defattr(644,root,root,755)
%{_libdir32}/libsupc++.la
%{_libdir32}/libsupc++.a
%endif

%files -n libstdc++ -f libstdc++.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libstdc++.so.*.*.*
%ifarch ppc
%attr(755,root,root) %{_libdir}/nof/libstdc++.so.*.*.*
%endif

%if %{with multilib}
%files -n libstdc++32
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir32}/libstdc++.so.*.*.*
%endif

%files -n libstdc++-devel
%defattr(644,root,root,755)
%doc libstdc++-v3/docs/html
%attr(755,root,root) %{_libdir}/libstdc++.so
%{_libdir}/libstdc++.la
%ifarch ppc
%attr(755,root,root) %{_libdir}/nof/libstdc++.so
%{_libdir}/nof/libstdc++.la
%endif
%dir %{_includedir}/c++
%{_includedir}/c++/%{GCC_VERSION}

%if %{with multilib}
%files -n libstdc++32-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir32}/libstdc++.so
%{_libdir32}/libstdc++.la
%endif

%files -n libstdc++-static
%defattr(644,root,root,755)
%{_libdir}/libstdc++.a
%ifarch ppc
%{_libdir}/nof/libstdc++.a
%endif

%if %{with multilib}
%files -n libstdc++32-static
%defattr(644,root,root,755)
%{_libdir32}/libstdc++.a
%endif
%endif

%if %{with objc}
%files objc
%defattr(644,root,root,755)
%doc gcc/objc/READ*
%attr(755,root,root) %{_libdir}/gcc-lib/*/*/cc1obj
%attr(755,root,root) %{_libdir}/libobjc.so
%{_libdir}/libobjc.la
%ifarch ppc
%attr(755,root,root) %{_libdir}/nof/libobjc.so
%{_libdir}/nof/libobjc.la
%endif
%{_libdir}/gcc-lib/*/*/include/objc

%if %{with multilib}
%files objc32
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir32}/libobjc.so
%{_libdir32}/libobjc.la
%endif

%files -n libobjc
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libobjc.so.*.*.*
%ifarch ppc
%attr(755,root,root) %{_libdir}/nof/libobjc.so.*.*.*
%endif

%if %{with multilib}
%files -n libobjc32
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir32}/libobjc.so.*.*.*
%endif

%files -n libobjc-static
%defattr(644,root,root,755)
%{_libdir}/libobjc.a
%ifarch ppc
%{_libdir}/nof/libobjc.a
%endif

%if %{with multilib}
%files -n libobjc32-static
%defattr(644,root,root,755)
%{_libdir32}/libobjc.a
%endif
%endif

%if %{with fortran}
%files g77
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/g77
%attr(755,root,root) %{_bindir}/f77
%{_infodir}/g77*
%attr(755,root,root) %{_libdir}/gcc-lib/*/*/f771
%{_libdir}/libfrtbegin.a
%{_libdir}/libg2c.la
%attr(755,root,root) %{_libdir}/libg2c.so
%ifarch ppc
%{_libdir}/nof/libfrtbegin.a
%{_libdir}/nof/libg2c.la
%attr(755,root,root) %{_libdir}/nof/libg2c.so
%endif
%{_libdir}/gcc-lib/*/*/include/g2c.h
%{_mandir}/man1/g77.1*
%{_mandir}/man1/f77.1*
%lang(ja) %{_mandir}/ja/man1/g77.1*
%lang(ja) %{_mandir}/ja/man1/f77.1*

%if %{with multilib}
%files g7732
%defattr(644,root,root,755)
%{_libdir32}/libfrtbegin.a
%{_libdir32}/libg2c.la
%attr(755,root,root) %{_libdir32}/libg2c.so
%endif

%files -n libg2c
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libg2c.so.*.*.*
%ifarch ppc
%attr(755,root,root) %{_libdir}/nof/libg2c.so.*.*.*
%endif

%if %{with multilib}
%files -n libg2c32
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir32}/libg2c.so.*.*.*
%endif

%files -n libg2c-static
%defattr(644,root,root,755)
%{_libdir}/libg2c.a
%ifarch ppc
%{_libdir}/nof/libg2c.a
%endif

%if %{with multilib}
%files -n libg2c32-static
%defattr(644,root,root,755)
%{_libdir32}/libg2c.a
%endif
%endif

%if %{with java}
%files java
%defattr(644,root,root,755)
%doc java-doc/*
%attr(755,root,root) %{_bindir}/gcj*
%attr(755,root,root) %{_bindir}/gij
%attr(755,root,root) %{_bindir}/jcf-dump
%attr(755,root,root) %{_bindir}/jv-*
%attr(755,root,root) %{_bindir}/*-gcj
%attr(755,root,root) %{_libdir}/gcc-lib/*/*/jc1
%attr(755,root,root) %{_libdir}/gcc-lib/*/*/jvgenmain
%{_infodir}/gcj*
%{_mandir}/man1/jcf-*
%{_mandir}/man1/jv-*
%{_mandir}/man1/gij*
%{_mandir}/man1/gcj*

%files java-tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/rmi*
%attr(755,root,root) %{_bindir}/jar
%attr(755,root,root) %{_bindir}/grepjar
%{_mandir}/man1/rmi*
%{_mandir}/man1/jar*
%{_mandir}/man1/grepjar*
%{_infodir}/fastjar*

%files -n libgcj
%defattr(644,root,root,755)
%doc libjava/LIBGCJ_LICENSE
%attr(755,root,root) %{_bindir}/addr2name.awk
%attr(755,root,root) %{_libdir}/lib*cj*.so.*.*.*
%attr(755,root,root) %{_libdir}/lib-org*.so.*.*.*
%ifarch ppc
%attr(755,root,root) %{_libdir}/nof/lib*cj*.so.*
%attr(755,root,root) %{_libdir}/nof/lib-org*.so.*
%endif

%if %{with multilib}
%files -n libgcj32
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir32}/lib*cj*.so.*.*.*
%attr(755,root,root) %{_libdir32}/lib-org*.so.*.*.*
%endif

%files -n libgcj-devel
%defattr(644,root,root,755)
%{_libdir}/gcc-lib/*/*/include/gcj
%dir %{_libdir}/security
%{_libdir}/security/*
%dir %{_datadir}/java
%{_datadir}/java/libgcj*.jar
%{_libdir}/lib*cj.spec
%attr(755,root,root) %{_libdir}/lib*cj*.so
%attr(755,root,root) %{_libdir}/lib-org-*.so
%{_libdir}/lib*cj*.la
%{_libdir}/lib-org-*.la
%ifarch ppc
%attr(755,root,root) %{_libdir}/nof/lib*cj*.so
%attr(755,root,root) %{_libdir}/nof/lib-org-*.so
%{_libdir}/nof/lib*cj*.la
%{_libdir}/nof/lib-org-*.la
%endif
%{_includedir}/java
%{_includedir}/javax
%{_includedir}/gcj
%{_includedir}/j*.h
%{_includedir}/gnu/*

%if %{with multilib}
%files -n libgcj32-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir32}/lib*cj*.so
%attr(755,root,root) %{_libdir32}/lib-org-*.so
%{_libdir32}/lib*cj*.la
%{_libdir32}/lib-org-*.la
%endif

%files -n libgcj-static
%defattr(644,root,root,755)
%{_libdir}/lib*cj*.a
%{_libdir}/lib-org-*.a
%ifarch ppc
%{_libdir}/nof/lib*cj*.a
%{_libdir}/nof/lib-org-*.a
%endif

%if %{with multilib}
%files -n libgcj32-static
%defattr(644,root,root,755)
%{_libdir32}/lib*cj*.a
%{_libdir32}/lib-org-*.a
%endif

%files -n libffi
%defattr(644,root,root,755)
%doc libffi/LICENSE
%attr(755,root,root) %{_libdir}/libffi-*.so
%ifarch ppc
%attr(755,root,root) %{_libdir}/nof/libffi-*.so
%endif

%if %{with multilib}
%files -n libffi32
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir32}/libffi-*.so
%endif

%files -n libffi-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libffi.so
%{_libdir}/libffi.la
%ifarch ppc
%attr(755,root,root) %{_libdir}/nof/libffi.so
%{_libdir}/nof/libffi.la
%endif
%{_includedir}/ffi*

%if %{with multilib}
%files -n libffi32-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir32}/libffi.so
%{_libdir32}/libffi.la
%endif

%files -n libffi-static
%defattr(644,root,root,755)
%{_libdir}/libffi.a
%ifarch ppc
%{_libdir}/nof/libffi.a
%endif

%if %{with multilib}
%files -n libffi32-static
%defattr(644,root,root,755)
%{_libdir32}/libffi.a
%endif
%endif

%if %{with ada}
%files ada
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gcc-lib/*/*/gnat1
%{_libdir}/gcc-lib/*/*/adainclude
%dir %{_libdir}/gcc-lib/*/*/adalib
%{_libdir}/gcc-lib/*/*/adalib/*.ali
%ifnarch ppc
%{_libdir}/gcc-lib/*/*/adalib/libgmem.a
%endif
%{_libdir}/gcc-lib/*/*/adalib/Makefile.adalib
%attr(755,root,root) %{_bindir}/gnat*
%{_infodir}/gnat*
%attr(755,root,root) %{_libdir}/libgnat*.so
%attr(755,root,root) %{_libdir}/libgnarl*.so

%files -n libgnat
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgna*.so.1

%files -n libgnat-static
%defattr(644,root,root,755)
%{_libdir}/gcc-lib/*/*/adalib/libgna*.a
%endif

%if %{with ksi}
%files ksi
%defattr(644,root,root,755)
%doc gcc/ksi/README gcc/ksi/NEWS gcc/ksi/t/*.{ksi,c,foo}
%{_infodir}/ksi*
%attr(755,root,root) %{_libdir}/gcc-lib/*/*/ksi1
%endif

%files -n cpp
%defattr(644,root,root,755)
%attr(755,root,root) /lib/cpp
%attr(755,root,root) %{_bindir}/cpp
%{_mandir}/man1/cpp.1*
%lang(ja) %{_mandir}/ja/man1/cpp.1*
%{_infodir}/cpp*
