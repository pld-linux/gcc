#
# Conditional build:
%bcond_without	ada		# build without ADA support
%bcond_without	java		# build without Java support
%bcond_without	objc		# build without objc support
%bcond_with	ssp		# build with stack-smashing protector support
#
%define		GCC_VERSION	3.4.1
%define		_snap		20040618
#
Summary:	GNU Compiler Collection: the C compiler and shared files
Summary(es):	Colección de compiladores GNU: el compilador C y ficheros compartidos
Summary(pl):	Kolekcja kompilatorów GNU: kompilator C i pliki wspó³dzielone
Summary(pt_BR):	Coleção dos compiladores GNU: o compilador C e arquivos compartilhados
Name:		gcc
Version:	%{GCC_VERSION}
Release:	0.%{_snap}.1
Epoch:		5
License:	GPL
Group:		Development/Languages
#Source0:	ftp://gcc.gnu.org/pub/gcc/releases/gcc-%{version}/%{name}-%{version}.tar.bz2
Source0:	ftp://gcc.gnu.org/pub/gcc/snapshots/3.4-%{_snap}/gcc-3.4-%{_snap}.tar.bz2
# Source0-md5:	6eb0e85c225250cc40b75496419d4250
Source1:	http://ep09.pld-linux.org/~djrzulf/gcc33/%{name}-non-english-man-pages.tar.bz2
# Source1-md5:	4736f3422ddfb808423b745629acc321
Source2:	http://www.trl.ibm.com/projects/security/ssp/gcc2_95_3/gcc_stack_protect.m4.gz
# Source2-md5:	07d93ad5fc07ca44cdaba46c658820de
Patch0:		%{name}-info.patch
Patch1:		%{name}-nolocalefiles.patch
Patch2:		%{name}-ada-link-new-libgnat.patch
Patch3:		%{name}-nodebug.patch
Patch4:		%{name}-ssp.patch

Patch6:		%{name}-ada-link.patch
Patch7:		%{name}-pr15666.patch
Patch8:		%{name}-ada-bootstrap.patch
URL:		http://gcc.gnu.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	binutils >= 2.15.90.0.3
BuildRequires:	bison
BuildRequires:	fileutils >= 4.0.41
BuildRequires:	flex
%if %{with ada}
BuildRequires:	gcc(ada)
BuildRequires:	gcc-ada
%endif
BuildRequires:	gettext-devel
BuildRequires:	glibc-devel >= 2.2.5-20
BuildRequires:	gzip
BuildRequires:	perl-devel
BuildRequires:	texinfo >= 4.1
BuildRequires:	zlib-devel
Requires:	binutils >= 2.15.90.0.3
Requires:	cpp = %{epoch}:%{version}-%{release}
Requires:	libgcc = %{epoch}:%{version}-%{release}
%{?with_ada:Provides:	gcc(ada)}
%{?with_ssp:Provides:	gcc(ssp)}
# ksi for gcc > 3.3.x not ready yet
Obsoletes:	gcc-ksi
Obsoletes:	gont
Conflicts:	glibc-devel < 2.2.5-20
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_slibdir	/%{_lib}
%ifarch sparc64
%define		_slibdir64	/lib64
%define		_libdir		/usr/lib
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
wyprodukowania szybkiego i stablinego kodu wynikowego.

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

%package -n libobjc
Summary:	Objective C Libraries
Summary(es):	Bibliotecas de Objective C
Summary(pl):	Biblioteki Obiektowego C
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
Group:		Development/Libraries
Requires:	libobjc = %{epoch}:%{version}-%{release}

%description -n libobjc-static
Static Objective C Libraries.

%description -n libobjc-static -l es
Bibliotecas estáticas de Objective C.

%description -n libobjc-static -l pl
Statyczne biblioteki Obiektowego C.

%package g77
Summary:	Fortran 77 support for gcc
Summary(es):	Soporte de Fortran 77 para gcc
Summary(pl):	Obs³uga Fortranu 77 dla gcc
Summary(pt_BR):	Suporte Fortran 77 para o GCC
Group:		Development/Languages/Fortran
Requires:	libg2c = %{epoch}:%{version}-%{release}
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

%package -n libg2c
Summary:	Fortran 77 Libraries
Summary(es):	Bibliotecas de Fortran 77
Summary(pl):	Biblioteki Fortranu 77
Group:		Libraries

%description -n libg2c
Fortran 77 Libraries.

%description -n libg2c -l es
Bibliotecas de Fortran 77.

%description -n libg2c -l pl
Biblioteki Fortranu 77.

%package -n libg2c-static
Summary:	Static Fortran 77 Libraries
Summary(es):	Bibliotecas estáticas de Fortran 77
Summary(pl):	Statyczne Biblioteki Fortranu 77
Group:		Development/Libraries
Requires:	libg2c = %{epoch}:%{version}-%{release}

%description -n libg2c-static
Static Fortran 77 Libraries.

%description -n libg2c -l es
Bibliotecas estáticas de Fortran 77.

%description -n libg2c-static -l pl
Statyczne biblioteki Fortranu 77.

%package java
Summary:	Java support for gcc
Summary(es):	Soporte de Java para gcc
Summary(pl):	Obs³uga Javy dla gcc
Group:		Development/Languages/Java
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	libgcj = %{epoch}:%{version}-%{release}
Requires:	libgcj-devel = %{epoch}:%{version}-%{release}
Requires:	java-shared
Provides:	gcj = %{epoch}:%{version}-%{release}

%description java
This package adds experimental support for compiling Java(tm) programs
and bytecode into native code. To use this you will also need the
libgcj package.

%description java -l es
Este paquete añade soporte experimental para compilar programas
Java(tm) y su bytecode en código nativo. Para usarlo también va a
necesitar el paquete libgcj.

%description java -l pl
Wsparcie dla kompilowania programów Java(tm) zrówno do bajt-kodu jak i
do natywnego kodu. Dodatkowo wymagany jest pakiet libgcj, aby mo¿na
by³o przeprowadziæ kompilacjê.

%package java-tools
Summary:	Shared java tools
Summary(es):	Herramientas compartidas de Java
Summary(pl):	Wspó³dzielone narzêdzia javy
Group:		Development/Languages/Java
Provides:	jar = %{epoch}:%{version}-%{release}
Provides:	java-shared
Obsoletes:	fastjar
Obsoletes:	java-shared
Obsoletes:	jar

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
Group:		Libraries
Requires:	zlib
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
Group:		Development/Libraries
Requires:	%{name}-java = %{epoch}:%{version}-%{release}
Requires:	libgcj = %{epoch}:%{version}-%{release}
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
Group:		Development/Libraries
Requires:	libgcj-devel = %{epoch}:%{version}-%{release}
Requires:	libstdc++-devel = %{epoch}:%{version}-%{release}

%description -n libgcj-static
Static Java Class Libraries.

%description -n libgcj-static -l es
Bibliotecas estáticas de clases de Java.

%description -n libgcj-static -l pl
Statyczne Biblioteki Klas Javy.

%package -n libstdc++
Summary:	GNU c++ library
Summary(es):	Biblioteca C++ de GNU
Summary(pl):	Biblioteki GNU C++
Summary(pt_BR):	Biblioteca C++ GNU
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
Group:		Development/Libraries
Requires:	%{name}-c++ = %{epoch}:%{version}-%{release}
Requires:	libstdc++ = %{epoch}:%{version}-%{release}
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
Group:		Development/Libraries
Requires:	libstdc++-devel = %{epoch}:%{version}-%{release}

%description -n libstdc++-static
Static C++ standard library.

%description -n libstdc++-static -l es
Biblioteca estándar estática de C++.

%description -n libstdc++-static -l pl
Statycza biblioteka standardowa C++.

%package -n libffi
Summary:	Foreign Function Interface library
Summary(es):	Biblioteca de interfaz de funciones ajenas
Summary(pl):	Biblioteka zewnêtrznych wywo³añ funkcji
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
Biblioteka libffi dostarcza przno¶nego, wysokopoziomowego
miêdzymordzia do ró¿nych konwencji wywo³añ funkcji. Pozwala to
programi¶cie wywo³ywaæ dowolne funkcje podaj±c konwencjê wywo³ania w
czasie wykonania.

%package -n libffi-devel
Summary:	Development files for Foreign Function Interface library
Summary(es):	Ficheros de desarrollo para libffi
Summary(pl):	Pliki nag³ówkowe dla libffi
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
Group:		Development/Libraries
Requires:	libffi-devel = %{epoch}:%{version}-%{release}

%description -n libffi-static
Static Foreign Function Interface library.

%description -n libffi-static -l es
Biblioteca libffi estática.

%description -n libffi-static -l pl
Statyczna biblioteka libffi.

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
Group:		Libraries
Obsoletes:	gnat-static

%description -n libgnat-static
This package contains static libraries for programs written in Ada.

%description -n libgnat-static -l pl
Ten pakiet zawiera biblioteki statyczne dla programów napisanych w
Adzie.

%package -n cpp
Summary:	The C Pre Processor
Summary(es):	El preprocesador de C
Summary(pl):	Preprocesor C
Summary(pt_BR):	Preprocessador para a linguagem C
Group:		Development/Languages
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
Przeprocesor C jest "makro procesorem" który jest automatycznie
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
%setup -q -n %{name}-3.4-%{_snap} -a1
%patch0 -p1
%patch1 -p1
%patch2 -p1
%{!?debug:%patch3 -p1}
%{?with_ssp:%patch4 -p1}
#patch5 -p1
%patch6 -p1
%patch7 -p0
%ifarch alpha
# only for bootstrap using gcc 3.3.x
%patch8 -p2
%endif

# because we distribute modified version of gcc...
perl -pi -e 's/(version.*)";/$1 %{?with_ssp:SSP }(PLD Linux)";/' gcc/version.c
perl -pi -e 's@(bug_report_url.*<URL:).*";@$1http://bugs.pld-linux.org/>";@' gcc/version.c

mv ChangeLog ChangeLog.general

%build
# cd gcc && autoconf; cd ..
# autoconf is not needed!
cp -f /usr/share/automake/config.sub .

rm -rf obj-%{_target_platform} && install -d obj-%{_target_platform} && cd obj-%{_target_platform}

CFLAGS="%{rpmcflags}" \
CXXFLAGS="%{rpmcflags}" \
TEXCONFIG=false ../configure \
	--prefix=%{_prefix} \
	--libdir=%{_libdir} \
	--libexecdir=%{_libexecdir} \
	--infodir=%{_infodir} \
	--mandir=%{_mandir} \
	--enable-shared \
	--enable-threads=posix \
	--enable-__cxa_atexit \
	--enable-languages="c,c++,f77%{?with_objc:,objc}%{?with_ada:,ada}%{?with_java:,java}" \
	--enable-c99 \
	--enable-long-long \
%ifarch amd64
	--disable-multilib \
%else
	--enable-multilib \
%endif
	--enable-nls \
	--with-gnu-as \
	--with-gnu-ld \
	--with-system-zlib \
	--with-slibdir=%{_slibdir} \
	--without-x \
	%{_target_platform}

PATH=$PATH:/sbin:%{_sbindir}

cd ..
%{__make} -C obj-%{_target_platform} profiledbootstrap \
	GCJFLAGS="%{rpmcflags}" \
	BOOT_CFLAGS="%{rpmcflags}" \
	STAGE1_CFLAGS="%{rpmcflags}" \
	LDFLAGS_FOR_TARGET="%{rpmldflags}" \
	mandir=%{_mandir} \
	infodir=%{_infodir}

%if %{with ada}
# cannot build it in parallel
for tgt in gnatlib-shared gnattools gnatlib; do
%{__make} -C obj-%{_target_platform}/gcc $tgt \
	BOOT_CFLAGS="%{rpmcflags}" \
	LDFLAGS_FOR_TARGET="%{rpmldflags}" \
	mandir=%{_mandir} \
	infodir=%{_infodir}
done
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/lib,%{_aclocaldir},%{_datadir},%{_infodir}}

cd obj-%{_target_platform}
PATH=$PATH:/sbin:%{_sbindir}

%{__make} install \
	mandir=%{_mandir} \
	infodir=%{_infodir} \
	DESTDIR=$RPM_BUILD_ROOT

%ifarch sparc64
ln -f $RPM_BUILD_ROOT%{_bindir}/sparc64-pld-linux-gcc \
	$RPM_BUILD_ROOT%{_bindir}/sparc-pld-linux-gcc
%endif

ln -sf gcc $RPM_BUILD_ROOT%{_bindir}/cc
echo ".so gcc.1" > $RPM_BUILD_ROOT%{_mandir}/man1/cc.1

ln -sf g77 $RPM_BUILD_ROOT%{_bindir}/f77
echo ".so g77.1" > $RPM_BUILD_ROOT%{_mandir}/man1/f77.1

%if %{with ada}
# move ada shared libraries to proper place...
mv -f $RPM_BUILD_ROOT%{_libdir}/gcc/*/*/adalib/*.so.1 \
	$RPM_BUILD_ROOT%{_libdir}
# check if symlink to be made is valid
test -f $RPM_BUILD_ROOT%{_libdir}/libgnat-3.4.so.1
ln -sf libgnat-3.4.so.1 $RPM_BUILD_ROOT%{_libdir}/libgnat-3.4.so
ln -sf libgnarl-3.4.so.1 $RPM_BUILD_ROOT%{_libdir}/libgnarl-3.4.so
ln -sf libgnat-3.4.so $RPM_BUILD_ROOT%{_libdir}/libgnat.so
ln -sf libgnarl-3.4.so $RPM_BUILD_ROOT%{_libdir}/libgnarl.so
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

# avoid -L poisoning in *.la - there should be only -L%{_libdir}/gcc/*/%{version}
for f in libstdc++.la libsupc++.la %{?with_java:libgcj.la} ; do
	perl -pi -e 's@-L[^ ]*[acs.] @@g' $RPM_BUILD_ROOT%{_libdir}/$f
done
# normalize libdir, to avoid propagation of unnecessary RPATHs by libtool
for f in libstdc++.la libsupc++.la libg2c.la \
	%{?with_java:libgcj.la lib-org-w3c-dom.la lib-org-xml-sax.la libffi.la} \
	%{?with_objc:libobjc.la}; do
	perl -pi -e "s@^libdir='.*@libdir='/usr/%{_lib}'@" $RPM_BUILD_ROOT%{_libdir}/$f
done

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}
mv -f $RPM_BUILD_ROOT%{_mandir}/ja/man1/{cccp,cpp}.1

# include/ contains install-tools/include/* and headers that were fixed up
# by fixincludes, we don't want former
gccdir=$(echo $RPM_BUILD_ROOT%{_libdir}/gcc/*/*/)
mkdir $gccdir/tmp
# we have to save these however
mv -f $gccdir/include/{%{?with_objc:objc,}g2c.h,syslimits.h%{?with_java:,gcj}} $gccdir/tmp
rm -rf $gccdir/include
mv -f $gccdir/tmp $gccdir/include
cp $gccdir/install-tools/include/*.h $gccdir/include
# but we don't want anything more from install-tools
rm -rf $gccdir/install-tools

%find_lang %{name}
%find_lang libstdc\+\+

%if %{with ssp}
zcat %{SOURCE2} > $RPM_BUILD_ROOT%{_aclocaldir}/gcc_stack_protect.m4
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

%files -f gcc.lang
%defattr(644,root,root,755)
%doc ChangeLog.general MAINTAINERS bugs.html faq.html
%doc gcc/{README.Portability,ONEWS,ChangeLog}
%dir %{_libdir}/gcc
%dir %{_libdir}/gcc/*
%dir %{_libdir}/gcc/*/*
%dir %{_libdir}/gcc/*/*/include
%{?with_ssp:%{_aclocaldir}/gcc_stack_protect.m4}
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

%attr(755,root,root) %{_slibdir}*/lib*.so
%{_libdir}/gcc/*/*/libgcov.a
%{_libdir}/gcc/*/*/libgcc.a
%{_libdir}/gcc/*/*/libgcc_eh.a
%{_libdir}/gcc/*/*/specs
%attr(644,root,root) %{_libdir}*/gcc/*/*/crt*.o
%ifarch sparc64
%{_libdir}/gcc/*/*/*/libgcc.a
%{_libdir}/gcc/*/*/*/libgcc_eh.a
%attr(644,root,root) %{_libdir}*/gcc/*/*/*/crt*.o
%endif
%ifarch ppc
%attr(644,root,root) %{_libdir}/gcc/*/*/ecrt*.o
%attr(644,root,root) %{_libdir}/gcc/*/*/ncrt*.o
%{_libdir}/gcc/*/*/nof
%dir %{_libdir}/nof
%endif
%attr(755,root,root) %{_libdir}/gcc/*/*/cc1
%attr(755,root,root) %{_libdir}/gcc/*/*/collect2

%{_libdir}/gcc/*/*/include/*.h
%exclude %{_libdir}/gcc/*/*/include/g2c.h

%files -n libgcc
%defattr(644,root,root,755)
%attr(755,root,root) %{_slibdir}*/lib*.so.*

%files c++
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/g++
%attr(755,root,root) %{_bindir}/*-g++
%attr(755,root,root) %{_bindir}/c++
%attr(755,root,root) %{_bindir}/*-c++
%attr(755,root,root) %{_libdir}/gcc/*/*/cc1plus
%{_libdir}*/libsupc++.la
%ifarch ppc
%{_libdir}/nof/libsupc++.la
%{_libdir}/nof/libsupc++.a
%endif
%{_libdir}*/libsupc++.a
%{_mandir}/man1/g++.1*
%lang(ja) %{_mandir}/ja/man1/g++.1*

%files -n libstdc++ -f libstdc++.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}*/libstdc++.so.*.*.*
%ifarch ppc
%attr(755,root,root) %{_libdir}/nof/libstdc++.so.*.*.*
%endif

%files -n libstdc++-devel
%defattr(644,root,root,755)
%doc libstdc++-v3/docs/html
%dir %{_includedir}/c++
%{_includedir}/c++/%{version}
%exclude %{_includedir}/c++/%{version}/*/bits/stdc++.h.gch
%attr(755,root,root) %{_libdir}*/libstdc++.so
%{_libdir}*/libstdc++.la
%ifarch ppc
%attr(755,root,root) %{_libdir}/nof/libstdc++.so
%{_libdir}/nof/libstdc++.la
%endif

%files -n libstdc++-static
%defattr(644,root,root,755)
%{_libdir}*/libstdc++.a
%ifarch ppc
%{_libdir}/nof/libstdc++.a
%endif

%if %{with objc}
%files objc
%defattr(644,root,root,755)
%doc gcc/objc/READ*
%attr(755,root,root) %{_libdir}/gcc/*/*/cc1obj
%attr(755,root,root) %{_libdir}*/libobjc.so
%{_libdir}*/libobjc.la
%ifarch ppc
%attr(755,root,root) %{_libdir}/nof/libobjc.so
%{_libdir}/nof/libobjc.la
%endif
%{_libdir}/gcc/*/*/include/objc

%files -n libobjc
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}*/libobjc.so.*.*.*
%ifarch ppc
%attr(755,root,root) %{_libdir}/nof/libobjc.so.*.*.*
%endif

%files -n libobjc-static
%defattr(644,root,root,755)
%{_libdir}*/libobjc.a
%ifarch ppc
%{_libdir}/nof/libobjc.a
%endif
%endif

%files g77
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/g77
%attr(755,root,root) %{_bindir}/f77
%{_infodir}/g77*
%attr(755,root,root) %{_libdir}/gcc/*/*/f771
%{_libdir}*/libfrtbegin.a
%{_libdir}*/libg2c.la
%attr(755,root,root) %{_libdir}*/libg2c.so
%ifarch ppc
%{_libdir}/nof/libfrtbegin.a
%{_libdir}/nof/libg2c.la
%attr(755,root,root) %{_libdir}/nof/libg2c.so
%endif
%{_libdir}/gcc/*/*/include/g2c.h
%{_mandir}/man1/g77.1*
%{_mandir}/man1/f77.1*
%lang(ja) %{_mandir}/ja/man1/g77.1*
%lang(ja) %{_mandir}/ja/man1/f77.1*

%files -n libg2c
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}*/libg2c.so.*.*.*
%ifarch ppc
%attr(755,root,root) %{_libdir}/nof/libg2c.so.*.*.*
%endif

%files -n libg2c-static
%defattr(644,root,root,755)
%{_libdir}*/libg2c.a
%ifarch ppc
%{_libdir}/nof/libg2c.a
%endif

%if %{with java}
%files java
%defattr(644,root,root,755)
%doc java-doc/*
%attr(755,root,root) %{_bindir}/gcj*
%attr(755,root,root) %{_bindir}/gij
%attr(755,root,root) %{_bindir}/jcf-dump
%attr(755,root,root) %{_bindir}/jv-*
%attr(755,root,root) %{_bindir}/grepjar
%attr(755,root,root) %{_bindir}/*-gcj*
%attr(755,root,root) %{_libdir}/gcc/*/*/jc1
%attr(755,root,root) %{_libdir}/gcc/*/*/jvgenmain
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
%{_libdir}/logging.properties

%files -n libgcj-devel
%defattr(644,root,root,755)
%{_includedir}/java
%{_includedir}/javax
%{_includedir}/gcj
%{_includedir}/j*.h
%{_includedir}/gnu/*
%{_libdir}/gcc/*/*/include/gcj
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
%{_pkgconfigdir}/libgcj.pc

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

%if %{with ada}
%files ada
%defattr(644,root,root,755)
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
%{_datadir}/gnat
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

%files -n cpp
%defattr(644,root,root,755)
%attr(755,root,root) /lib/cpp
%attr(755,root,root) %{_bindir}/cpp
%{_mandir}/man1/cpp.1*
%lang(ja) %{_mandir}/ja/man1/cpp.1*
%{_infodir}/cpp*
