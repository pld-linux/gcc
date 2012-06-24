#
# Conditional build:
# _without_ada	- build without ADA support
# _without_java	- build without Java support
# _without_objc	- build without objc support

%define		DASHED_SNAP	%{nil}
%define		SNAP		%(echo %{DASHED_SNAP} | sed -e "s#-##g")
%define		GCC_VERSION	3.3.1
%define		KSI_VERSION	1.1.0.1567

Summary:	GNU C Compiler
Summary(pl):	Kompilator C GNU
Summary(pt_BR):	C Compilador GNU (GCC)
Name:		gcc
Version:	%{GCC_VERSION}
Release:	1
Epoch:		5
License:	GPL
Group:		Development/Languages
Source0:	ftp://gcc.gnu.org/pub/gcc/releases/gcc-%{GCC_VERSION}/%{name}-%{GCC_VERSION}.tar.bz2
# Source0-md5:	1135a104e9fa36fdf7c663598fab5c40
Source1:	ftp://ftp.pld-linux.org/people/malekith/ksi/ksi-%{KSI_VERSION}.tar.gz
# Source1-md5:	66f07491b44f06928fd95b0e65bb8cd3
Source2:	http://ep09.kernel.pl/~djrzulf/gcc33/%{name}-non-english-man-pages.tar.bz2
# Source2-md5: 4736f3422ddfb808423b745629acc321
Patch0:		%{name}-info.patch
Patch1:		%{name}-paths.patch
Patch2:		%{name}-nolocalefiles.patch
Patch3:		%{name}-ada-link-new-libgnat.patch
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
#Patch25:	%{name}-unwind.patch	-- obsolete?
BuildRequires:	autoconf
BuildRequires:	binutils >= 2.14
BuildRequires:	bison
BuildRequires:	fileutils >= 4.0.41
BuildRequires:	gcc
%{!?_without_ada:BuildRequires:	gcc-ada}
BuildRequires:	glibc-devel >= 2.2.5-20
BuildRequires:	perl-devel
BuildRequires:	texinfo >= 4.1
BuildRequires:	zlib-devel
BuildRequires:	gettext-devel
Requires:	binutils >= 2.14
Requires:	cpp = %{epoch}:%{GCC_VERSION}
Requires:	libgcc = %{epoch}:%{GCC_VERSION}
Conflicts:	glibc-devel < 2.2.5-20
URL:		http://gcc.gnu.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_slibdir	/lib

%description
A compiler aimed at integrating all the optimizations and features
necessary for a high-performance and stable development environment.

%description -l pl
Kompilator, posiadaj�cy du�e mo�liwo�ci optymalizacyjne niezb�dne do
wyprodukowania szybkiego i stablinego kodu wynikowego.

%description -l pt_BR
Este pacote adiciona infraestrutura b�sica e suporte a linguagem C
ao Gnu Compiler Collection.

%package -n libgcc
Summary:	Shared gcc library
Summary(pl):	Biblioteka gcc
Summary(pt_BR):	Biblioteca runtime para o GCC
Group:		Libraries
Version:	%{GCC_VERSION}
Obsoletes:	libgcc1

%description -n libgcc
Shared gcc library.

%description -n libgcc -l pl
Biblioteka dynamiczna gcc.

%description -n libgcc -l pt_BR
Biblioteca runtime para o GCC.

%package c++
Summary:	C++ support for gcc
Summary(pl):	Obs�uga C++ dla gcc
Summary(pt_BR):	Suporte C++ para o gcc
Group:		Development/Languages
Obsoletes:	egcc-c++
Obsoletes:	egcs-c++
Requires:	gcc = %{epoch}:%{GCC_VERSION}

%description c++
This package adds C++ support to the GNU C compiler. It includes
support for most of the current C++ specification, including templates
and exception handling. It does not include a standard C++ library,
which is available separately.

%description c++ -l de
Dieses Paket enth�lt die C++-Unterst�tzung f�r den GNU-C-Compiler. Es
unterst�tzt die aktuelle C++-Spezifikation, inkl. Templates und
Ausnahmeverarbeitung. Eine C++-Standard-Library ist nicht enthalten -
sie ist getrennt erh�ltlich.

%description c++ -l fr
Ce package ajoute un support C++ au compilateur c GNU. Il comprend un
support pour la plupart des sp�cifications actuelles de C++, dont les
mod�les et la gestion des exceptions. Il ne comprend pas une
biblioth�que C++ standard, qui est disponible s�par�ment.

%description c++ -l pl
Ten pakiet dodaje obs�ug� C++ do kompilatora gcc. Ma wsparcie dla
du�ej ilo�ci obecnych specyfikacji C++, nie zawiera natomiast
standardowych bibliotek C++, kt�re s� w oddzielnym pakiecie.

%description c++ -l pt_BR
Este pacote adiciona suporte C++ para o gcc.

%description c++ -l tr
Bu paket, GNU C derleyicisine C++ deste�i ekler. 'Template'ler ve
ayk�r� durum i�leme gibi �o�u g�ncel C++ tan�mlar�na uyar. Standart
C++ kitapl��� bu pakette yer almaz.

%package objc
Summary:	Objective C support for gcc
Summary(de):	Objektive C-Unterst�tzung f�r gcc
Summary(fr):	Gestion d'Objective C pour gcc
Summary(pl):	Obs�uga obiektowego C dla kompilatora gcc
Summary(tr):	gcc i�in Objective C deste�i
Group:		Development/Languages
Obsoletes:	egcc-objc
Obsoletes:	egcs-objc
Requires:	libobjc = %{epoch}:%{GCC_VERSION}
Requires:	gcc = %{epoch}:%{GCC_VERSION}

%description objc
This package adds Objective C support to the GNU C compiler. Objective
C is a object oriented derivative of the C language, mainly used on
systems running NeXTSTEP. This package does not include the standard
objective C object library.

%description objc -l de
Dieses Paket erg�nzt den GNU-C-Compiler durch Objective-C-Support.
Objective C ist ein objektorientiertes Derivat von C, das zur
Hauptsache auf Systemen mit NeXTSTEP zum Einsatz kommt. Die
Standard-Objective-C-Objekt-Library ist nicht Teil des Pakets.

%description objc -l fr
Ce package ajoute un support Objective C au compilateur C GNU.
L'Objective C est un langage orient� objetd�riv� du langage C,
principalement utilis� sur les syst�mes NeXTSTEP. Ce package n'inclue
pas la biblioth�que Objective C standard.

%description objc -l pl
Ten pakiet dodaje obs�ug� obiektowego C do kompilatora gcc. Obiektowe
C (objc) jest zorientowan� obiektowo pochodn� j�zyka C, u�ywan�
g��wnie w systemach u�ywaj�cych NeXTSTEP. W pakiecie nie ma
standardowej biblioteki objc (kt�ra znajduje si� w osobnym pakiecie).

%description objc -l tr
Bu paket, GNU C derleyicisine Objective C deste�i ekler. Objective C,
C dilinin nesne y�nelik bir t�revidir ve NeXTSTEP alt�nda �al��an
sistemlerde yayg�n olarak kullan�l�r. Standart Objective C nesne
kitapl��� bu pakette yer almaz.

%package -n libobjc
Summary:	Objective C Libraries
Summary(pl):	Biblioteki Obiektowego C
Group:		Libraries
Version:	%{GCC_VERSION}
Obsoletes:	libobjc1

%description -n libobjc
Objective C Libraries.

%description -n libobjc -l pl
Biblioteki Obiektowego C.

%package -n libobjc-static
Summary:	Static Objective C Libraries
Summary(pl):	Statyczne Biblioteki Obiektowego C
Group:		Development/Libraries
Version:	%{GCC_VERSION}
Requires:	libobjc = %{epoch}:%{GCC_VERSION}

%description -n libobjc-static
Static Objective C Libraries.

%description -n libobjc-static -l pl
Statyczne biblioteki Obiektowego C.

%package g77
Summary:	Fortran 77 support for gcc
Summary(pl):	Obs�uga Fortranu 77 dla gcc
Summary(pt_BR):	Suporte Fortran 77 para o GCC
Group:		Development/Languages/Fortran
Version:	%{GCC_VERSION}
Obsoletes:	egcs-g77
Requires:	libg2c = %{epoch}:%{GCC_VERSION}

%description g77
This apckage adds support for compiling Fortran 77 programs with the
GNU compiler.

%description g77 -l pl
Ten pakiet dodaje obs�ug� Fortranu 77 do kompilatora gcc. Jest
potrzebny do kompilowania program�w pisanych w j�zyku Fortran 77.

%description g77 -l pt_BR
Suporte Fortran 77 para o GCC.

%package -n libg2c
Summary:	Fortran 77 Libraries
Summary(pl):	Biblioteki Fortranu 77
Group:		Libraries
Version:	%{GCC_VERSION}

%description -n libg2c
Fortran 77 Libraries.

%description -n libg2c -l pl
Biblioteki Fortranu 77.

%package -n libg2c-static
Summary:	Static Fortran 77 Libraries
Summary(pl):	Statyczne Biblioteki Fortranu 77
Group:		Development/Libraries
Version:	%{GCC_VERSION}
Requires:	libg2c = %{epoch}:%{GCC_VERSION}

%description -n libg2c-static
Static Fortran 77 Libraries.

%description -n libg2c-static -l pl
Statyczne biblioteki Fortranu 77.

%package java
Summary:	Java support for gcc
Summary(pl):	Obs�uga Javy dla gcc
Group:		Development/Languages/Java
Version:	%{GCC_VERSION}
Requires:	%{name} = %{epoch}:%{version}
Requires:	libgcj >= 3.0.0
Requires:	libgcj-devel >= 3.0.0
Requires:	java-shared
Provides:	gcj = %{epoch}:%{GCC_VERSION}-%{release}

%description java
This package adds experimental support for compiling Java(tm) programs
and bytecode into native code. To use this you will also need the
libgcj package.

%description -l pl java
Wsparcie dla kompilowania program�w Java(tm) zr�wno do bajt-kodu jak i
do natywnego kodu. Dodatkowo wymagany jest pakiet libgcj, aby mo�na
by�o przeprowadzi� kompilacj�.

%package java-tools
Summary:	Shared java tools
Summary(pl):	Wsp�dzielone narz�dzia javy
Group:		Development/Languages/Java
Version:	%{GCC_VERSION}
Provides:	jar = %{epoch}:%{GCC_VERSION}-%{release}
Provides:	java-shared
Obsoletes:	fastjar
Obsoletes:	java-shared
Obsoletes:	jar

%description java-tools
This package contains tools that are common for every Java(tm) implementation,
such as rmic or jar.

%description java-tools -l pl
Pakiet ten zawiera narz�dzia wsp�lne dla ka�dej implementacji Javy(tm), takie
jak rmic czy jar.

%package -n libgcj
Summary:	Java Class Libraries
Summary(pl):	Biblioteki Klas Javy
Group:		Libraries
Version:	%{GCC_VERSION}
Requires:	zlib
Obsoletes:	libgcj3

%description -n libgcj
Java Class Libraries.

%description -n libgcj -l pl
Biblioteki Klas Javy.

%package -n libgcj-devel
Summary:	Development files for Java Class Libraries
Summary(pl):	Pliki nag��wkowe dla Bibliotek Klas Javy
Group:		Development/Libraries
Version:	%{GCC_VERSION}
Requires:	libgcj = %{epoch}:%{GCC_VERSION}
Requires:	%{name}-java
Obsoletes:	libgcj3-devel

%description -n libgcj-devel
Development files for Java Class Libraries.

%description -n libgcj-devel -l pl
Pliki nag��wkowe dla Bibliotek Klas Javy.

%package -n libgcj-static
Summary:	Static Java Class Libraries
Summary(pl):	Statyczne Biblioteki Klas Javy
Group:		Development/Libraries
Version:	%{GCC_VERSION}
Requires:	libstdc++-devel = %{epoch}:%{GCC_VERSION}
Requires:	libgcj-devel = %{epoch}:%{GCC_VERSION}

%description -n libgcj-static
Static Java Class Libraries.

%description -n libgcj-static -l pl
Statyczne Biblioteki Klas Javy.

%package -n libstdc++
Summary:	GNU c++ library
Summary(pl):	Biblioteki GNU C++
Summary(pt_BR):	Biblioteca C++ GNU
Group:		Libraries
Version:	%{GCC_VERSION}
Obsoletes:	libg++
Obsoletes:	libstdc++3

%description -n libstdc++
This is the GNU implementation of the standard C++ libraries, along
with additional GNU tools. This package includes the shared libraries
necessary to run C++ applications.

%description -n libstdc++ -l de
Dies ist die GNU-Implementierung der Standard-C++-Libraries mit
weiteren GNU-Tools. Dieses Paket enth�lt die zum Ausf�hren von
C++-Anwendungen erforderlichen gemeinsam genutzten Libraries.

%description -n libstdc++ -l es
Este es el soporte de las bibliotecas padr�n del C++, junto con
herramientas GNU adicionales. El paquete incluye las bibliotecas
compartidas necesarias para ejecutar aplicaciones C++.

%description -n libstdc++ -l fr
Ceci est l'impl�mentation GNU des librairies C++ standard, ainsi que
des outils GNU suppl�mentaires. Ce package comprend les librairies
partag�es n�cessaires � l'ex�cution d'application C++.

%description -n libstdc++ -l pl
Pakiet ten zawiera biblioteki b�d�ce implementacj� standardowych
bibliotek C++. Znajduj� si� w nim biblioteki dynamiczne niezb�dne do
uruchomienia aplikacji napisanych w C++.

%description -n libstdc++ -l pt_BR
Este pacote � uma implementa��o da biblioteca padr�o C++ v3, um
subconjunto do padr�o ISO 14882.

%description -n libstdc++ -l tr
Bu paket, standart C++ kitapl�klar�n�n GNU ger�eklemesidir ve C++
uygulamalar�n�n ko�turulmas� i�in gerekli kitapl�klar� i�erir.

%package -n libstdc++-devel
Summary:	Header files and documentatino for C++ development
Summary(de):	Header-Dateien zur Entwicklung mit C++
Summary(fr):	Fichiers d'en-t�te et biblitoth�ques pour d�velopper en C++
Summary(pl):	Pliki nag��wkowe i dokumentacja do biblioteki standardowej C++
Summary(pt_BR):	Arquivos de inclus�o e bibliotecas para o desenvolvimento em C++
Summary(tr):	C++ ile program geli�tirmek i�in gerekli dosyalar
Group:		Development/Libraries
Version:	%{GCC_VERSION}
Requires:	libstdc++ = %{epoch}:%{GCC_VERSION}
Requires:	%{name}-c++ = %{epoch}:%{GCC_VERSION}
Obsoletes:	libg++-devel
Obsoletes:	libstdc++3-devel

%description -n libstdc++-devel
This is the GNU implementation of the standard C++ libraries. This
package includes the header files needed for C++ development and
library documentation.

%description -n libstdc++-devel -l es
Este es el soporte de las bibliotecas padr�n del lenguaje C++. Este paquete
incluye los archivos de inclusi�n y bibliotecas necesarios para desarrollo de
programas en lenguaje C++.

%description -n libstdc++-devel -l pl
Pakiet ten zawiera biblioteki b�d�ce implementacj� standardowych
bibliotek C++. Znajduj� si� w nim pliki nag��wkowe wykorzystywane przy
programowaniu w j�zyku C++ oraz dokumentacja biblioteki standardowej.

%description -n libstdc++-devel -l pt_BR
Este pacote inclui os arquivos de inclus�o e bibliotecas necess�rias para
desenvolvimento de programas C++.

%package -n libstdc++-static
Summary:	Static C++ standard library
Summary(pl):	Statyczna biblioteka standardowa C++
Group:		Development/Libraries
Version:	%{GCC_VERSION}
Requires:	libstdc++-devel = %{epoch}:%{GCC_VERSION}

%description -n libstdc++-static
Static C++ standard library.

%description -n libstdc++-static -l pl
Statycza biblioteka standardowa C++.

%package -n libffi
Summary:	Foreign Function Interface library
Summary(pl):	Biblioteka zewn�trznych wywo�a� funkcji
Group:		Libraries
Version:	%{GCC_VERSION}

%description -n libffi
The libffi library provides a portable, high level programming
interface to various calling conventions. This allows a programmer to
call any function specified by a call interface description at run
time.

%description -n libffi -l pl
Biblioteka libffi dostarcza przno�nego, wysokopoziomowego mi�dzymordzia
do r�nych konwencji wywo�a� funkcji. Pozwala to programi�cie wywo�ywa�
dowolne funkcje podaj�c konwencj� wywo�ania w czasie wykonania.

%package -n libffi-devel
Summary:	Development files for Foreign Function Interface library
Summary(pl):	Pliki nag��wkowe dla libffi
Group:		Development/Libraries
Version:	%{GCC_VERSION}
Requires:	libffi = %{epoch}:%{GCC_VERSION}

%description -n libffi-devel
Development files for Foreign Function Interface library.

%description -n libffi-devel -l pl
Pliki nag��wkowe dla libffi.

%package -n libffi-static
Summary:	Static Foreign Function Interface library
Summary(pl):	Statyczna biblioteka libffi
Group:		Development/Libraries
Version:	%{GCC_VERSION}
Requires:	libffi-devel = %{epoch}:%{GCC_VERSION}

%description -n libffi-static
Static Foreign Function Interface library.

%description -n libffi-static -l pl
Statyczna biblioteka libffi.

%package ada
Summary:	Ada support for gcc
Summary(pl):	Obs�uga Ady do gcc
Group:		Development/Languages
Version:	%{GCC_VERSION}
Requires:	libgnat = %{epoch}:%{GCC_VERSION}
Requires:	gcc = %{epoch}:%{GCC_VERSION}
Obsoletes:	gcc-gnat
Obsoletes:	gnat-devel

%description ada
This package adds experimental support for compiling Ada programs.

%description -l pl ada
Ten pakiet dodaje eksperymentalne wsparcie dla kompilacji program�w
w Adzie.

%package -n libgnat
Summary:	Ada standard libraries
Summary(pl):	Biblioteki standardowe dla Ady
Group:		Libraries
Version:	%{GCC_VERSION}
Obsoletes:	gnat
Obsoletes:	libgnat1

%description -n libgnat
This package contains shared libraries needed to run programs written
in Ada.

%description -n libgnat -l pl
Ten pakiet zawiera biblioteki potrzebne do uruchamiania program�w napisanych
w Adzie.

%package -n libgnat-static
Summary:	Static Ada standard libraries
Summary(pl):	Statyczne biblioteki standardowe dla Ady
Group:		Libraries
Version:	%{GCC_VERSION}
Obsoletes:	gnat-static

%description -n libgnat-static
This package contains static libraries for programs written in Ada.

%description -n libgnat-static -l pl
Ten pakiet zawiera biblioteki statyczne dla program�w napisanych w
Adzie.

%package ksi
Summary:	Ksi support for gcc
Summary(pl):	Obs�uga Ksi dla gcc
Version:	%{GCC_VERSION}.%{KSI_VERSION}
Group:		Development/Languages
Requires:	gcc = %{epoch}:%{GCC_VERSION}

%description ksi
This package adds experimental support for compiling Ksi programs
into native code. You proabably don't need it, unless your are going
to develop a compiler using Ksi as intermediate representation or
you are using such compiler (like Gont).

%description ksi -l pl
Ten pakiet dodaje eksperymentalne wsparcie dla kompilacji program�w
w Ksi do kodu maszynowego. Prawdopodobnie nie potrzebujesz go, chyba
�e zamierzasz pisa� kompilator u�ywaj�cy Ksi jako reprezentacji
po�rednicz�cej, lub u�ywasz takiego kompilatora (jak Gont).

%package -n cpp
Summary:	The C Pre Processor
Summary(pl):	Preprocesor C
Summary(pt_BR):	Preprocessador para a linguagem C
Group:		Development/Languages
Version:	%{GCC_VERSION}
Obsoletes:	egcs-cpp
Obsoletes:	gcc-cpp

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
Um preprocessador para a linguagem C.

%description -n cpp -l pl
Przeprocesor C jest "makro procesorem" kt�ry jest automatycznie
u�ywany przez kompilator C do obr�bki kompilowanego programu przed
w�a�ciw� kompilacj�. Jest on nazywany makroprocesorem, poniewa�
umo�liwia definiowanie i rozwijanie makr umo�liwiaj�cych skracanie
d�ugich konstrukcji w j�zyku C.

Preprocesor C umo�liwia wykonywanie czterech r�nych typ�w operacji:

- Do��czanie plik�w (np. nag��wkowych). Wstawia pliki w miejscu
  deklaracji polecenia do��czenia innego pliku.
- Rozwijanie makr. Mo�na definiowa� "makra" nadaj�c im identyfikatory,
  kt�rych p�niejsze u�ycie powoduje podczas rozwijania podmienienie
  indentyfikatora deklarowan� wcze�niej warto�ci�.
- Kompilacja warunkowa. W zale�no�ci od obecno�ci symboli i dyrektyw w
  �rodowisku preprocesora s� w��czane warunkowo, b�d� nie, pewne
  fragmenty obrabianego strumienia tekst�w.
- Kontrola linii �r�d�a. Niezale�nie od tego jakim przeobra�eniom
  podlega wynikowy strumie� danych w wyniku rozwijania makr i do��czania
  s� zapami�tywane informacje o tym, kt�rej linii pliku �r�d�owego
  odpowiada fragment pliku wynikowego.

%description  -n cpp -l pt_BR
O preprocessador C � um "processador de macros", que � utilizado pelo
compilador C para fazer algumas modifica��es no seu programa, antes da
compila��o em si. Ele � chamado de "processador de macros" porque
permite a voc� definir "macros", que s�o abrevia��es para constru��es
mais complicadas.

O preprocessador C fornece quatro funcionalidades b�sicas: inclus�o de
arquivos de cabe�alho; expans�o de macros; compila��o condicional;
e controle da numera��o das linhas do programa.

%prep
%setup -q -a1 -n %{name}-%{GCC_VERSION}
mv ksi-%{KSI_VERSION} gcc/ksi

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

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

# because we distribute modified version of gcc...
perl -pi -e 's/(version.*)";/$1 (PLD Linux)";/' gcc/version.c
perl -pi -e 's@(bug_report_url.*<URL:).*";@$1http://bugs.pld-linux.org/>";@' gcc/version.c

%build
# cd gcc && autoconf; cd ..
# autoconf is not needed!
rm -rf obj-%{_target_platform} && install -d obj-%{_target_platform} && cd obj-%{_target_platform}

CFLAGS="%{rpmcflags}" \
CXXFLAGS="%{rpmcflags}" \
TEXCONFIG=false ../configure \
	--prefix=%{_prefix} \
	--infodir=%{_infodir} \
	--mandir=%{_mandir} \
	--enable-shared \
	--enable-threads=posix \
	--enable-__cxa_atexit \
	--enable-languages="c,c++,f77%{!?_without_objc:,objc}%{!?_without_ada:,ada}%{!?_without_java:,java},ksi" \
	--enable-c99 \
	--enable-long-long \
	--enable-multilib \
	--enable-nls \
	--with-gnu-as \
	--with-gnu-ld \
	--with-system-zlib \
	--with-slibdir=%{_slibdir} \
	--without-x \
	%{_target_platform}

PATH=$PATH:/sbin:%{_sbindir}

cd ..
%{__make} -C obj-%{_target_platform} bootstrap-lean \
	LDFLAGS_FOR_TARGET="%{rpmldflags}" \
	mandir=%{_mandir} \
	infodir=%{_infodir}

%if 0%{!?_without_ada:1}
%{__make} -C obj-%{_target_platform}/gcc gnatlib gnattools gnatlib-shared \
	LDFLAGS_FOR_TARGET="%{rpmldflags}" \
	mandir=%{_mandir} \
	infodir=%{_infodir}
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/lib,%{_datadir},%{_infodir}}

cd obj-%{_target_platform}
PATH=$PATH:/sbin:%{_sbindir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

ln -sf gcc $RPM_BUILD_ROOT%{_bindir}/cc
echo ".so gcc.1" > $RPM_BUILD_ROOT%{_mandir}/man1/cc.1

ln -sf g77 $RPM_BUILD_ROOT%{_bindir}/f77
echo ".so g77.1" > $RPM_BUILD_ROOT%{_mandir}/man1/f77.1

%if 0%{!?_without_ada:1}
# move ada shared libraries to proper place...
mv $RPM_BUILD_ROOT%{_libdir}/gcc-lib/%{_target_cpu}*/*/adalib/*.so.1 \
	$RPM_BUILD_ROOT%{_libdir}/
# check if symlink to be made is valid
test -f $RPM_BUILD_ROOT%{_libdir}/libgnat-3.15.so.1
ln -sf libgnat-3.15.so.1 $RPM_BUILD_ROOT%{_libdir}/libgnat-3.15.so
ln -sf libgnarl-3.15.so.1 $RPM_BUILD_ROOT%{_libdir}/libgnarl-3.15.so
ln -sf libgnat-3.15.so $RPM_BUILD_ROOT%{_libdir}/libgnat.so
ln -sf libgnarl-3.15.so $RPM_BUILD_ROOT%{_libdir}/libgnarl.so
%endif

ln -sf %{_bindir}/cpp $RPM_BUILD_ROOT/lib/cpp

cd ..

%if %{!?_without_java:1}%{?_without_java:0}
install -d java-doc
cp -f libjava/doc/cni.sgml libjava/READ* java-doc
cp -f fastjar/README java-doc/README.fastjar
cp -f libffi/README java-doc/README.libffi
cp -f libffi/LICENSE java-doc/LICENSE.libffi
%endif

%if %{!?_without_objc:1}0
cp -f libobjc/README gcc/objc/README.libobjc
%endif

# avoid -L poisoning in *.la - there should be only -L%{_libdir}/gcc-lib/*/%{version}
for f in libstdc++.la libsupc++.la %{!?_without_java:libgcj.la} ; do
	perl -pi -e 's@-L[^ ]*[acs.] @@g' $RPM_BUILD_ROOT%{_libdir}/$f
done
# normalize libdir, to avoid propagation of unnecessary RPATHs by libtool
for f in libstdc++.la libsupc++.la libg2c.la \
	%{!?_without_java:libgcj.la lib-org-w3c-dom.la lib-org-xml-sax.la libffi.la} \
	%{!?_without_objc:libobjc.la}; do
	perl -pi -e "s@^libdir='.*@libdir='/usr/lib'@" $RPM_BUILD_ROOT%{_libdir}/$f
done

bzip2 -dc %{SOURCE2} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}
mv -f $RPM_BUILD_ROOT%{_mandir}/ja/man1/{cccp,cpp}.1

# include/ contains install-tools/include/* and headers that were fixed up
# by fixincludes, we don't want former
gccdir=$(echo $RPM_BUILD_ROOT%{_libdir}/gcc-lib/%{_target_cpu}*/*/)
mkdir $gccdir/tmp
# we have to save these however
mv -f $gccdir/include/{%{!?_without_objc:objc,}g2c.h,syslimits.h%{!?_without_java:,gcj}} $gccdir/tmp
rm -rf $gccdir/include
mv -f $gccdir/tmp $gccdir/include
cp $gccdir/install-tools/include/*.h $gccdir/include
# but we don't want anything more from install-tools
rm -rf $gccdir/install-tools/

%find_lang %{name}
%find_lang libstdc\+\+

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
%post   -p /sbin/ldconfig -n libstdc++
%postun -p /sbin/ldconfig -n libstdc++
%post   -p /sbin/ldconfig -n libobjc
%postun -p /sbin/ldconfig -n libobjc
%post   -p /sbin/ldconfig -n libg2c
%postun -p /sbin/ldconfig -n libg2c
%post   -p /sbin/ldconfig -n libgcj
%postun -p /sbin/ldconfig -n libgcj
%post   -p /sbin/ldconfig -n libgnat
%postun -p /sbin/ldconfig -n libgnat
%post   -p /sbin/ldconfig -n libffi
%postun -p /sbin/ldconfig -n libffi

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc READ* ChangeLog
%dir %{_libdir}/gcc-lib
%dir %{_libdir}/gcc-lib/%{_target_cpu}*
%dir %{_libdir}/gcc-lib/%{_target_cpu}*/*
%dir %{_libdir}/gcc-lib/%{_target_cpu}*/*/include
%attr(755,root,root) %{_bindir}/%{_target_cpu}*-gcc
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
%{_libdir}/gcc-lib/%{_target_cpu}*/*/libgcc.a
%{_libdir}/gcc-lib/%{_target_cpu}*/*/libgcc_eh.a
%{_libdir}/gcc-lib/%{_target_cpu}*/*/specs
%attr(644,root,root) %{_libdir}/gcc-lib/%{_target_cpu}*/*/crt*.o
%ifarch ppc
%attr(644,root,root) %{_libdir}/gcc-lib/%{_target_cpu}*/*/ecrt*.o
%attr(644,root,root) %{_libdir}/gcc-lib/%{_target_cpu}*/*/ncrt*.o
%{_libdir}/gcc-lib/%{_target_cpu}*/*/nof
%dir %{_libdir}/nof
%endif
%attr(755,root,root) %{_libdir}/gcc-lib/%{_target_cpu}*/*/cc1
%attr(755,root,root) %{_libdir}/gcc-lib/%{_target_cpu}*/*/collect2

%{_libdir}/gcc-lib/%{_target_cpu}*/*/include/*.h
%exclude %{_libdir}/gcc-lib/%{_target_cpu}*/*/include/g2c.h

%files -n libgcc
%defattr(644,root,root,755)
%attr(755,root,root) %{_slibdir}/lib*.so.*

%files c++
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/g++
%attr(755,root,root) %{_bindir}/%{_target_cpu}*-g++
%attr(755,root,root) %{_bindir}/c++
%attr(755,root,root) %{_bindir}/%{_target_cpu}*-c++
%attr(755,root,root) %{_libdir}/gcc-lib/%{_target_cpu}*/*/cc1plus
%{_libdir}/libsupc++.la
%ifarch ppc
%{_libdir}/nof/libsupc++.la
%{_libdir}/nof/libsupc++.a
%endif
%{_libdir}/libsupc++.a
%{_mandir}/man1/g++.1*
%lang(ja) %{_mandir}/ja/man1/g++.1*

%files -n libstdc++ -f libstdc++.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libstdc++.so.*.*.*
%ifarch ppc
%attr(755,root,root) %{_libdir}/nof/libstdc++.so.*.*.*
%endif

%files -n libstdc++-devel
%defattr(644,root,root,755)
%doc libstdc++-v3/docs/html
%dir %{_includedir}/c++
%{_includedir}/c++/%{GCC_VERSION}
%attr(755,root,root) %{_libdir}/libstdc++.so
%{_libdir}/libstdc++.la
%ifarch ppc
%attr(755,root,root) %{_libdir}/nof/libstdc++.so
%{_libdir}/nof/libstdc++.la
%endif

%files -n libstdc++-static
%defattr(644,root,root,755)
%{_libdir}/libstdc++.a
%ifarch ppc
%{_libdir}/nof/libstdc++.a
%endif

%if %{!?_without_objc:1}0
%files objc
%defattr(644,root,root,755)
%doc gcc/objc/READ*
%attr(755,root,root) %{_libdir}/gcc-lib/%{_target_cpu}*/*/cc1obj
%attr(755,root,root) %{_libdir}/libobjc.so
%{_libdir}/libobjc.la
%ifarch ppc
%attr(755,root,root) %{_libdir}/nof/libobjc.so
%{_libdir}/nof/libobjc.la
%endif
%{_libdir}/gcc-lib/%{_target_cpu}*/*/include/objc

%files -n libobjc
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libobjc.so.*.*.*
%ifarch ppc
%attr(755,root,root) %{_libdir}/nof/libobjc.so.*.*.*
%endif

%files -n libobjc-static
%defattr(644,root,root,755)
%{_libdir}/libobjc.a
%ifarch ppc
%{_libdir}/nof/libobjc.a
%endif
%endif

%files g77
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/g77
%attr(755,root,root) %{_bindir}/f77
%{_infodir}/g77*
%attr(755,root,root) %{_libdir}/gcc-lib/%{_target_cpu}*/*/f771
%{_libdir}/libfrtbegin.a
%{_libdir}/libg2c.la
%attr(755,root,root) %{_libdir}/libg2c.so
%ifarch ppc
%{_libdir}/nof/libfrtbegin.a
%{_libdir}/nof/libg2c.la
%attr(755,root,root) %{_libdir}/nof/libg2c.so
%endif
%{_libdir}/gcc-lib/%{_target_cpu}*/*/include/g2c.h
%{_mandir}/man1/g77.1*
%{_mandir}/man1/f77.1*
%lang(ja) %{_mandir}/ja/man1/g77.1*
%lang(ja) %{_mandir}/ja/man1/f77.1*

%files -n libg2c
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libg2c.so.*.*.*
%ifarch ppc
%attr(755,root,root) %{_libdir}/nof/libg2c.so.*.*.*
%endif

%files -n libg2c-static
%defattr(644,root,root,755)
%{_libdir}/libg2c.a
%ifarch ppc
%{_libdir}/nof/libg2c.a
%endif

%if %{!?_without_java:1}%{?_without_java:0}
%files java
%defattr(644,root,root,755)
%doc java-doc/*
%attr(755,root,root) %{_bindir}/gcj*
%attr(755,root,root) %{_bindir}/gij
%attr(755,root,root) %{_bindir}/jcf-dump
%attr(755,root,root) %{_bindir}/jv-*
%attr(755,root,root) %{_bindir}/grepjar
%attr(755,root,root) %{_bindir}/%{_target_cpu}*-gcj
%attr(755,root,root) %{_libdir}/gcc-lib/%{_target_cpu}*/*/jc1
%attr(755,root,root) %{_libdir}/gcc-lib/%{_target_cpu}*/*/jvgenmain
%{_infodir}/gcj*
%{_mandir}/man1/jcf-*
%{_mandir}/man1/jv-*
%{_mandir}/man1/gij*
%{_mandir}/man1/gcj*
%{_mandir}/man1/grepjar*

%files java-tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/rmi*
%attr(755,root,root) %{_bindir}/jar
%{_mandir}/man1/rmi*
%{_mandir}/man1/jar*
%{_infodir}/fastjar*

%files -n libgcj
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/addr2name.awk
%attr(755,root,root) %{_libdir}/lib*cj*.so.*.*.*
%attr(755,root,root) %{_libdir}/lib-org*.so.*.*.*
%ifarch ppc
%attr(755,root,root) %{_libdir}/nof/lib*cj*.so.*
%endif

%files -n libgcj-devel
%defattr(644,root,root,755)
%{_includedir}/java
%{_includedir}/javax
#%%{_includedir}/org
%{_includedir}/gcj
%{_includedir}/j*.h
%{_includedir}/gnu/*
%{_libdir}/gcc-lib/%{_target_cpu}*/*/include/gcj
%dir %{_libdir}/security
%{_libdir}/security/*
%dir %{_datadir}/java
%{_datadir}/java/libgcj*.jar
%{_libdir}/lib*cj.spec
%{_libdir}/lib*cj*.la
%attr(755,root,root) %{_libdir}/lib*cj*.so
%attr(755,root,root) %{_libdir}/lib-org-*.so
%{_libdir}/lib-org-*.la
%ifarch ppc
%{_libdir}/nof/lib*cj*.la
%attr(755,root,root) %{_libdir}/nof/lib*cj*.so
%endif

%files -n libgcj-static
%defattr(644,root,root,755)
%{_libdir}/lib*cj*.a
%{_libdir}/lib-org-*.a
%ifarch ppc
%{_libdir}/nof/lib*cj*.a
%endif

%files -n libffi
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libffi-*.so

%files -n libffi-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libffi.so
%{_libdir}/libffi.la
%{_includedir}/ffi*

%files -n libffi-static
%defattr(644,root,root,755)
%{_libdir}/libffi.a
%endif

%if 0%{!?_without_ada:1}
%files ada
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gcc-lib/%{_target_cpu}*/*/gnat1
%{_libdir}/gcc-lib/%{_target_cpu}*/*/adainclude
%dir %{_libdir}/gcc-lib/%{_target_cpu}*/*/adalib
%{_libdir}/gcc-lib/%{_target_cpu}*/*/adalib/*.ali
%ifnarch ppc
%{_libdir}/gcc-lib/%{_target_cpu}*/*/adalib/libgmem.a
%endif
%{_libdir}/gcc-lib/%{_target_cpu}*/*/adalib/Makefile.adalib
%attr(755,root,root) %{_bindir}/gnat*
%{_infodir}/gnat*
%attr(755,root,root) %{_libdir}/libgnat*.so
%attr(755,root,root) %{_libdir}/libgnarl*.so

%files -n libgnat
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgna*.so.1

%files -n libgnat-static
%defattr(644,root,root,755)
%{_libdir}/gcc-lib/%{_target_cpu}*/*/adalib/libgna*.a
%endif

%files ksi
%defattr(644,root,root,755)
%doc gcc/ksi/README gcc/ksi/NEWS gcc/ksi/t/*.{ksi,c,foo}
%{_infodir}/ksi*
%attr(755,root,root) %{_libdir}/gcc-lib/%{_target_cpu}*/*/ksi1

%files -n cpp
%defattr(644,root,root,755)
%attr(755,root,root) %{_slibdir}/cpp
%attr(755,root,root) %{_bindir}/cpp
%{_mandir}/man1/cpp.1*
%lang(ja) %{_mandir}/ja/man1/cpp.1*
%{_infodir}/cpp*
