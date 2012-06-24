%define		STDC_VERSION 2.10.0
%define		GCJ_VERSION 2.95.1
Summary:	GNU C Compiler
Summary(pl):	Kompilator GNU
Name:		gcc
Version:	2.95.2
Release:	1
Copyright:	GPL
Group:		Development/Languages
Group(pl):	Programowanie/J�zyki
Source0:	ftp://ftp.gnu.org/pub/gnu/gcc/%{name}-%{version}.tar.bz2
Source1:	ftp://sourceware.cygnus.com/pub/java/libgcj-%{GCJ_VERSION}.tar.gz
Patch0:		gcc-info.patch
Patch1:		gcc-libgcj-config.patch
Patch2:		gcc-pld-linux.patch
Patch3:		gcc-libstdc++.patch
Requires:	binutils >= 2.9.1.0.25
Requires:	cpp 
Prereq:		/usr/sbin/fix-info-dir
URL:		http://www.gnu.org/
BuildRoot:	/tmp/%{name}-%{version}-root

%description
A compiler aimed at integrating all the optimizations and features
necessary for a high-performance and stable development environment.

%description -l pl
Kompilator, posiadaj�cy du�e mo�liwo�ci optymalizacyjne niezb�dne do
wyprodukowania szybkiego i stablinego kodu wynikowego.

%package c++
Summary:	C++ support for gcc
Summary(fr):	Support C++ pour le compilateur gcc.
Summary(pl):	Wspomaganie C++ dla kompilatora gcc
Summary(tr):	gcc i�in C++ deste�i
Group:		Development/Languages
Group(pl):	Programowanie/J�zyki
Obsoletes:	egcc-c++

%description c++
This package adds C++ support to the GNU C compiler. It includes support
for most of the current C++ specification, including templates and
exception handling. It does not include a standard C++ library, which
is available separately.

%description -l de c++
Dieses Paket enth�lt die C++-Unterst�tzung f�r den GNU-C-Compiler. Es
unterst�tzt die aktuelle C++-Spezifikation, inkl. Templates und
Ausnahmeverarbeitung. Eine C++-Standard-Library ist nicht enthalten - sie ist
getrennt erh�ltlich.

%description -l fr c++
Ce package ajoute un support C++ au compilateur c GNU. Il comprend un
support pour la plupart des sp�cifications actuelles de C++, dont les 
mod�les et la gestion des exceptions. Il ne comprend pas une biblioth�que
C++ standard, qui est disponible s�par�ment.

%description -l pl c++
Programy z tego pakietu zapewniaj� wsparcie do C++ do GNU C kompilatora.
Posiada wspomaganie dla du�ej ilo�ci obecnych specyfikacji C++, nie posiada
natomiast standardowych bibliotek C++, kt�re s� w oddzielnym pakiecie.

%description -l tr c++
Bu paket, GNU C derleyicisine C++ deste�i ekler. 'Template'ler ve ayk�r� durum
i�leme gibi �o�u g�ncel C++ tan�mlar�na uyar. Standart C++ kitapl��� bu
pakette yer almaz.

%package objc
Summary:	Objective C support for gcc
Summary(de):	Objektive C-Unterst�tzung f�r gcc
Summary(fr):	Gestion d'Objective C pour gcc
Summary(pl):	Wspomaganie obiektowego C dla kompilatora gcc
Summary(tr):	gcc i�in Objective C deste�i
Group:		Development/Languages
Group(pl):	Programowanie/J�zyki
Obsoletes:	egcc-objc

%description objc
This package adds Objective C support to the GNU C compiler. Objective C is
a object oriented derivative of the C language, mainly used on systems
running NeXTSTEP. This package does not include the standard objective C
object library.

%description -l de objc
Dieses Paket erg�nzt den GNU-C-Compiler durch Objective-C-Support. Objective
C ist ein objektorientiertes Derivat von C, das zur Hauptsache auf Systemen
mit NeXTSTEP zum Einsatz kommt. Die Standard-Objective-C-Objekt-Library ist
nicht Teil des Pakets.

%description -l fr objc
Ce package ajoute un support Objective C au compilateur C GNU. L'Objective C
est un langage orient� objetd�riv� du langage C, principalement utilis� sur
les syst�mes NeXTSTEP. Ce package n'inclue pas la biblioth�que Objective C
standard.

%description -l pl objc
Ten pakiet jest wsparciem obiektowego C dla kompilatora gcc.  W pakiecie nie
ma jeszcze bibliotek C-obj.

%description -l tr objc
Bu paket, GNU C derleyicisine Objective C deste�i ekler. Objective C, C
dilinin nesne y�nelik bir t�revidir ve NeXTSTEP alt�nda �al��an sistemlerde
yayg�n olarak kullan�l�r. Standart Objective C nesne kitapl��� bu pakette
yer almaz.

%package g77
Summary:	Fortran 77 support for gcc
Summary(pl):	Wspomaganie Fortran 77 dla gcc
Group:		Development/Languages
Group(pl):	Programowanie/J�zyki
Prereq:		/usr/sbin/fix-info-dir

%description g77
This apckage adds support for compiling Fortran 77 programs with the GNU
compiler.

%description -l pl g77
Ten pakiet jest wspomaganiem Fortran 77 dla kompilatora gcc.
Jest u�yteczny kompilowania program�w pisanych w j�zyku Fortran 77.

%package chill
Summary:	CHILL support for gcc
Summary(pl):	Wspomoganie CHILL dla gcc
Group:		Development/Languages
Group(pl):	Programowanie/J�zyki
Requires:	%{name} = %{version}
Prereq:		/usr/sbin/fix-info-dir

%description chill
This package adds support for compiling CHILL programs with the GNU
compiler.

Chill is the "CCITT High-Level Language", where CCITT is the old
name for what is now ITU, the International Telecommunications Union.
It is is language in the Modula2 family, and targets many of the
same applications as Ada (especially large embedded systems).
Chill was never used much in the United States, but is still
being used in Europe, Brazil, Korea, and other places.

%package java
Summary:	Java support for gcc
Summary(pl):	Wspomoganie Java dla gcc
Group:		Development/Languages
Group(pl):	Programowanie/J�zyki
Requires:	%{name} = %{version}
Requires:	%{name}-libgcj = %{version}

%description java
This package adds experimental support for compiling Java(tm) programs and
bytecode into native code. To use this you will also need the gcc-libgcj
package.

%package libgcj
Summary:	Java runtime library for gcc
Group:		Libraries
URL:		http://sourceware.cygnus.com/java/
Requires:	zip >= 2.1

%description libgcj
The Java runtime library. You will need this package to compile your Java
programs using the gcc Java compiler (gcj).

%package libgcj-static
Summary:	Static java runtime library for gcc
Group:		Development/Libraries
URL:		http://sourceware.cygnus.com/java/
Requires:	%{name}-libgcj = %{version}

%description libgcj-static
The static java runtime library. You will need this package to staticly
compile your Java programs using the gcc Java compiler (gcj).

%package -n libstdc++
Summary:	GNU c++ library
Summary(pl):	Biblioteki GNU C++ 
Group:		Libraries
Group(pl):	Biblioteki
Version:	%{STDC_VERSION}
Obsoletes:	libg++

%description -n libstdc++
This is the GNU implementation of the standard C++ libraries, along with
additional GNU tools. This package includes the shared libraries
necessary to run C++ applications.

%description -l de -n libstdc++
Dies ist die GNU-Implementierung der Standard-C++-Libraries mit weiteren
GNU-Tools. Dieses Paket enth�lt die zum Ausf�hren von C++-Anwendungen
erforderlichen gemeinsam genutzten Libraries.

%description -l fr -n libstdc++
Ceci est l'impl�mentation GNU des librairies C++ standard, ainsi que des
outils GNU suppl�mentaires. Ce package comprend les librairies partag�es
n�cessaires � l'ex�cution d'application C++.

%description -l pl -n libstdc++  
Pakiet ten zawiera biblioteki b�d�ce inplementacj� standardowych bibliotek
C++, znajduj� si� w nim biblioteki dynamiczne niezb�dne do uruchomienia
aplikacji C++.

%description -l tr -n libstdc++
Bu paket, standart C++ kitapl�klar�n�n GNU ger�eklemesidir ve C++
uygulamalar�n�n ko�turulmas� i�in gerekli kitapl�klar� i�erir.

%package -n libstdc++-devel
Summary:	Header files and libraries for C++ development
Summary(de):	Header-Dateien und Libraries zur Entwicklung mit C++
Summary(fr):	Fichiers d'en-t�te et biblitoth�ques pour d�velopper en C++.
Summary(tr):	C++ ile program geli�tirmek i�in gerekli dosyalar
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Version:	%{STDC_VERSION}
Requires:	libstdc++ = %{STDC_VERSION}
Obsoletes:	libg++-devel

%description -n libstdc++-devel
This is the GNU implementation of the standard C++ libraries.  This package
includes the header files and libraries needed for C++ development.

%description -l pl -n libstdc++-devel
Pakiet ten zawiera biblioteki b�d�ce inplementacj� standardowych bibliotek
C++, znajduj� si� w nim biblioteki i pliki nag��wk�w wykorzystywane do
programowania w j�zyku C++.

%package -n libstdc++-static
Summary:	Static c++ standard library
Summary(pl):	Biblioeka statyczna c++
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Version:	%{STDC_VERSION}
Requires:	libstdc++-devel = %{STDC_VERSION}

%description -n libstdc++-static
Static c++ standard library.

%description -l pl -n libstdc++-static
Biblioeka statyczna c++.

%package -n cpp
Summary:	The C Pre Processor
Summary(pl):	Preprocesor C
Group:		Development/Languages
Group(pl):	Programowanie/J�zyki
Prereq:		/usr/sbin/fix-info-dir
Obsoletes:	egcs-cpp

%description -n cpp
The C preprocessor is a "macro processor" that is used automatically by the
C compiler to transform your program before actual compilation. It is called
a macro processor because it allows you to define "macros", which are brief
abbreviations for longer constructs.

The C preprocessor provides four separate facilities that you can use as you
see fit:

* Inclusion of header files.  These are files of declarations that
  can be substituted into your program.
* Macro expansion.  You can define "macros", which are abbreviations for
  arbitrary fragments of C code, and then the C preprocessor will replace
  the macros with their definitions throughout the program.
* Conditional compilation.  Using special preprocessing directives,
  you can include or exclude parts of the program according to various
  conditions.
* Line control.  If you use a program to combine or rearrange source
  files into an intermediate file which is then compiled, you can use line
  control to inform the compiler of where each source line originally came
  from.

%description -l pl -n cpp
Przeprocesor C jest "makro procesorem" kt�ry jest automatycznie u�ywaney
przez kompilator C do obr�bki kompilowanego programu przed w�a�ciw�
kompilacj�. Jest on nazywany makroprocesorem poniewa� poniewa� umo�liwia
definiowanie i rozwijanie makr umo�liwiaj�cych kracanie d�ugich konstrukcji
w j�zyku C.

Preprocesor C umo�liwia wykonywanie czterech r�znych typow operacji:

* Inkluzja (do�aczenie) plik�w (np. nag��wkowych). W��cza pliki w miejscu
  deklaracji polecenia do��czenia inefgo pliku.
* Rozwijanie makr. Mo�na definiowa� "makra" nadaj�c im identyfikatory,
  kt�rych p�niejsze u�ycie powoduje podczas rozwijania podmienienie
  indentyfikatora deklarowan� wcze�niej warto�ci�.
* Kompilacja warunkowa. W zale�no�ci od obecno�ci symboli i dyrektyw w
  �rodowisku preprocesora s� w��czane warunkowo b�� nie pewne fragmenty
  obrabianego strumienia tekst�w.
* Kontrola linii �r�d�a. Niezale�nie od tego jakim przeobra�eniom podlega
  wynikowy strumie� danych w wyniku rozwijania makr i inkluzji s�
  zapami�tywane informacje o tym z kt�rej linii pliku �r�d�owego
  odpowiada fragment czy liniia pliku wynikowego.

%prep
%setup -q
%setup -q -a1 -D -T
mv libgcj-%{GCJ_VERSION} libgcj
mv libgcj/boehm-gc libgcj/libjava libgcj/zlib libgcj/zip .
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
rm -rf obj-%{_target_platform}
install -d obj-%{_target_platform} && cd obj-%{_target_platform} 

CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
../configure \
	--prefix=%{_prefix} \
	--infodir=%{_infodir} \
	--enable-shared \
	--enable-threads \
	--enable-haifa \
	--with-gnu-as \
	--with-gnu-ld \
	--with-gxx-include-dir="\$\{prefix\}/include/g++" \
	%{_target_platform}

PATH=$PATH:/sbin:%{_sbindir}
touch  ../gcc/c-gperf.h

make LDFLAGS_FOR_TARGET="-s" \
	bootstrap-lean \
	mandir=%{_mandir} \
	infodir=%{_infodir}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}

cd obj-%{_target_platform}
PATH=$PATH:/sbin:%{_sbindir}

make install \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	mandir=$RPM_BUILD_ROOT%{_mandir} \
	infodir=$RPM_BUILD_ROOT%{_infodir}

make install \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	mandir=$RPM_BUILD_ROOT%{_mandir} \
	infodir=$RPM_BUILD_ROOT%{_infodir} -C texinfo

strip $RPM_BUILD_ROOT%{_bindir}/* || :

strip $RPM_BUILD_ROOT%{_libdir}/gcc-lib/%{_target_cpu}*/*/{cc1,cc1chill,cc1obj,cc1plus,cpp,f771,collect2,jc1,jvgenmain}
strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/libstdc++.so.*.*.*

ln -sf gcc $RPM_BUILD_ROOT%{_bindir}/cc

echo .so g77.1 > $RPM_BUILD_ROOT%{_mandir}/man1/f77.1
echo .so cccp.1 > $RPM_BUILD_ROOT%{_mandir}/man1/cpp.1

ln -sf g77 $RPM_BUILD_ROOT%{_bindir}/f77

(cd $RPM_BUILD_ROOT%{_libdir} ; ln -sf libstdc++.so.*.*.* $RPM_BUILD_ROOT%{_libdir}/libstdc++.so)

install -d $RPM_BUILD_ROOT/lib
(cd $RPM_BUILD_ROOT; \
ln -sf ../`dirname usr/lib/gcc-lib/%{_target_cpu}*/*/cpp`/cpp $RPM_BUILD_ROOT/lib/cpp)

gzip -9nf $RPM_BUILD_ROOT%{_datadir}/{info/*.info*,man/man1/*} \
	  ../READ* ../ChangeLog ../gcc/ch/chill.brochure

%post
/usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
/usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%post g77
/usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun g77
/usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%post chill
/usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun chill
/usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%post -n cpp
/usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun -n cpp
/usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%post libgcj  -p /sbin/ldconfig

%post   -p /sbin/ldconfig -n libstdc++
%postun -p /sbin/ldconfig -n libstdc++

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc READ* ChangeLog.gz

%dir %{_libdir}/gcc-lib
%dir %{_libdir}/gcc-lib/%{_target_cpu}*
%dir %{_libdir}/gcc-lib/%{_target_cpu}*/*
%dir %{_libdir}/gcc-lib/%{_target_cpu}*/*/include

%attr(755,root,root) %{_bindir}/%{_target_cpu}*-gcc
%attr(755,root,root) %{_bindir}/gcc
%attr(755,root,root) %{_bindir}/gcov
%attr(755,root,root) %{_bindir}/protoize
%attr(755,root,root) %{_bindir}/unprotoize
%attr(755,root,root) %{_bindir}/cc

%{_mandir}/man1/gcc.1*
%{_infodir}/gcc*

%{_libdir}/gcc-lib/%{_target_cpu}*/*/SYSCALLS.c.X
%attr(755,root,root) %{_libdir}/gcc-lib/%{_target_cpu}*/*/cc1
%{_libdir}/gcc-lib/%{_target_cpu}*/*/libgcc.a
%{_libdir}/gcc-lib/%{_target_cpu}*/*/lib*.map
%{_libdir}/gcc-lib/%{_target_cpu}*/*/specs

%ifnarch alpha
%attr(755,root,root) %{_libdir}/gcc-lib/%{_target_cpu}*/*/crt*.o
%endif

%attr(755,root,root) %{_libdir}/gcc-lib/%{_target_cpu}*/*/collect2

%{_libdir}/gcc-lib/%{_target_cpu}*/*/include/float.h
%{_libdir}/gcc-lib/%{_target_cpu}*/*/include/iso646.h
%{_libdir}/gcc-lib/%{_target_cpu}*/*/include/limits.h
%{_libdir}/gcc-lib/%{_target_cpu}*/*/include/proto.h
%{_libdir}/gcc-lib/%{_target_cpu}*/*/include/stdarg.h
%{_libdir}/gcc-lib/%{_target_cpu}*/*/include/stdbool.h
%{_libdir}/gcc-lib/%{_target_cpu}*/*/include/stddef.h
%{_libdir}/gcc-lib/%{_target_cpu}*/*/include/syslimits.h
%{_libdir}/gcc-lib/%{_target_cpu}*/*/include/va-*.h
%{_libdir}/gcc-lib/%{_target_cpu}*/*/include/varargs.h

%files c++
%defattr(644,root,root,755)

%{_mandir}/man1/g++.1.gz

%attr(755,root,root) %{_bindir}/g++
%attr(755,root,root) %{_bindir}/c++
%attr(755,root,root) %{_bindir}/c++filt
%attr(755,root,root) %{_libdir}/gcc-lib/%{_target_cpu}*/*/cc1plus

%{_libdir}/gcc-lib/%{_target_cpu}*/*/include/exception
%{_libdir}/gcc-lib/%{_target_cpu}*/*/include/new
%{_libdir}/gcc-lib/%{_target_cpu}*/*/include/typeinfo
%{_libdir}/gcc-lib/%{_target_cpu}*/*/include/new.h

%files objc
%defattr(644,root,root,755)

%attr(755,root,root) %{_libdir}/gcc-lib/%{_target_cpu}*/*/cc1obj

%{_libdir}/gcc-lib/%{_target_cpu}*/*/libobjc.a
%{_libdir}/gcc-lib/%{_target_cpu}*/*/include/objc

%files g77
%defattr(644,root,root,755)

%attr(755,root,root) %{_bindir}/g77
%attr(755,root,root) %{_bindir}/f77

%{_infodir}/g77*

%attr(755,root,root) %{_libdir}/gcc-lib/%{_target_cpu}*/*/f771
%{_libdir}/gcc-lib/%{_target_cpu}*/*/libg2c.a

%{_mandir}/man1/g77.1*
%{_mandir}/man1/f77.1*

%{_libdir}/gcc-lib/%{_target_cpu}*/*/include/g2c.h

%files chill
%defattr(644,root,root,755)
%doc gcc/ch/chill.brochure.gz

%attr(755,root,root) %{_bindir}/chill

%{_infodir}/chill*

%attr(755,root,root) %{_libdir}/gcc-lib/%{_target_cpu}*/*/cc1chill
%attr(755,root,root) %{_libdir}/gcc-lib/%{_target_cpu}*/*/chill*.o
%{_libdir}/gcc-lib/%{_target_cpu}*/*/libchill.a

%files java
%defattr(644,root,root,755)

%attr(755,root,root) %{_bindir}/gcj
%attr(755,root,root) %{_bindir}/gcjh
%attr(755,root,root) %{_bindir}/jcf-dump
%attr(755,root,root) %{_bindir}/jv-convert
%attr(755,root,root) %{_bindir}/jv-scan

%{_libdir}/*.spec

%attr(755,root,root) %{_libdir}/gcc-lib/%{_target_cpu}*/*/jc1
%attr(755,root,root) %{_libdir}/gcc-lib/%{_target_cpu}*/*/jvgenmain

%files libgcj
%defattr(644,root,root,755)

%attr(755,root,root) %{_libdir}/lib*gcj*.so
%attr(755,root,root) %{_libdir}/lib*gcj*.so.*.*.*

%files libgcj-static
%defattr(644,root,root,755)

%{_libdir}/lib*gcj*.a
%{_libdir}/lib*gcj*.la

%files -n libstdc++
%attr(755,root,root) %{_libdir}/libstdc++.so.*.*.*

%files -n libstdc++-devel
%defattr(644,root,root,755) 
%{_includedir}/g++
%attr(755,root,root) %{_libdir}/libstdc++.so

%files -n libstdc++-static
%attr(644,root,root) %{_libdir}/libstdc++.a

%files -n cpp
%defattr(644,root,root,755)
%attr(755,root,root) /lib/cpp

%{_mandir}/man1/cpp.1*
%{_mandir}/man1/cccp.1*
%{_infodir}/cpp.info*.gz

%attr(755,root,root) %{_libdir}/gcc-lib/%{_target_cpu}*/*/cpp
