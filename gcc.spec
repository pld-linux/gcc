%define		STDC_VERSION 2.10.0
%define		ver 2.95.3
Summary:	GNU Compiler Collection
Summary(pl):	Kolekcja kompilatorów GNU
Name:		gcc
Version:	%{ver}
Release:	19
License:	GPL
Group:		Development/Languages
Group(de):	Entwicklung/Sprachen
Group(pl):	Programowanie/Jêzyki
Source0:	ftp://gcc.gnu.org/pub/gcc/releases/gcc-%{version}-prerelease/%{name}-%{version}.test2.tar.gz
Source1:	gcov.1
Patch0:		%{name}-info.patch
Patch1:		%{name}-pld-linux.patch
Patch2:		%{name}-libstdc++.patch
Patch3:		%{name}-bootstrap.patch
Patch4:		%{name}-cpp-macro-doc.patch
Patch5:		%{name}-default-arch.patch
Patch6:		%{name}-cvs-updates-20000826.patch.gz
Patch7:		%{name}-libstdc++-out-of-mem.patch
Patch8:		%{name}-libstdc++-wstring.patch
Patch9:		%{name}-libstdc++-wall3.patch
Patch10:	%{name}-libstdc++-bastring.patch
Patch11:	%{name}-manpage.patch
Patch12:	%{name}-cpp-dos-newlines.patch
Patch13:	%{name}-gpc.patch
Patch14:	%{name}-arm-config.patch
Patch15:	%{name}-m68k-pic.patch
Patch16:	%{name}-sparc32-rfi.patch
Patch17:	%{name}-builtin-apply.patch
Patch18:	%{name}-gcj-backport.patch
Patch19:	%{name}-ppc-ice.patch
Patch20:	%{name}-ppc-descriptions.patch
Patch21:	%{name}-ppc-andrew-dwarf-eh.patch

Patch22:	%{name}-alpha-complex-float.patch
Patch23:	%{name}-emit-rtl.patch
Patch24:	%{name}-gcj-vs-iconv.patch
Patch25:	%{name}-libobjc.patch
Patch26:	%{name}-pointer-arith.patch

Patch27:	%{name}-glibc-2.2.patch
Patch28:	%{name}-O2-bug.patch

BuildRequires:	bison
BuildRequires:	texinfo
Requires:	binutils >= 2.9.1.0.25
Requires:	cpp = %{version}
URL:		http://gcc.gnu.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A compiler aimed at integrating all the optimizations and features
necessary for a high-performance and stable development environment.

%description -l pl
Kompilator, posiadaj±cy du¿e mo¿liwo¶ci optymalizacyjne niezbêdne do
wyprodukowania szybkiego i stablinego kodu wynikowego.

%package c++
Summary:	C++ support for gcc
Summary(fr):	Support C++ pour le compilateur gcc
Summary(pl):	Wspomaganie C++ dla kompilatora gcc
Summary(tr):	gcc için C++ desteði
Group:		Development/Languages
Group(de):	Entwicklung/Sprachen
Group(pl):	Programowanie/Jêzyki
Obsoletes:	egcc-c++
Obsoletes:	egcs-c++

%description c++
This package adds C++ support to the GNU C compiler. It includes
support for most of the current C++ specification, including templates
and exception handling. It does not include a standard C++ library,
which is available separately.

%description -l de c++
Dieses Paket enthält die C++-Unterstützung für den GNU-C-Compiler. Es
unterstützt die aktuelle C++-Spezifikation, inkl. Templates und
Ausnahmeverarbeitung. Eine C++-Standard-Library ist nicht enthalten -
sie ist getrennt erhältlich.

%description -l fr c++
Ce package ajoute un support C++ au compilateur c GNU. Il comprend un
support pour la plupart des spécifications actuelles de C++, dont les
modéles et la gestion des exceptions. Il ne comprend pas une
bibliothéque C++ standard, qui est disponible séparément.

%description -l pl c++
Programy z tego pakietu zapewniaj± wsparcie dla C++ do gcc. Posiada
wspomaganie dla du¿ej ilo¶ci obecnych specyfikacji C++, nie posiada
natomiast standardowych bibliotek C++, które s± w oddzielnym pakiecie.

%description -l tr c++
Bu paket, GNU C derleyicisine C++ desteði ekler. 'Template'ler ve
aykýrý durum iþleme gibi çoðu güncel C++ tanýmlarýna uyar. Standart
C++ kitaplýðý bu pakette yer almaz.

%package objc
Summary:	Objective C support for gcc
Summary(de):	Objektive C-Unterstützung für gcc
Summary(fr):	Gestion d'Objective C pour gcc
Summary(pl):	Wspomaganie obiektowego C dla kompilatora gcc
Summary(tr):	gcc için Objective C desteði
Group:		Development/Languages
Group(de):	Entwicklung/Sprachen
Group(pl):	Programowanie/Jêzyki
Obsoletes:	egcc-objc
Obsoletes:	egcs-objc

%description objc
This package adds Objective C support to the GNU C compiler. Objective
C is a object oriented derivative of the C language, mainly used on
systems running NeXTSTEP. This package does not include the standard
objective C object library.

%description -l de objc
Dieses Paket ergänzt den GNU-C-Compiler durch Objective-C-Support.
Objective C ist ein objektorientiertes Derivat von C, das zur
Hauptsache auf Systemen mit NeXTSTEP zum Einsatz kommt. Die
Standard-Objective-C-Objekt-Library ist nicht Teil des Pakets.

%description -l fr objc
Ce package ajoute un support Objective C au compilateur C GNU.
L'Objective C est un langage orienté objetdérivé du langage C,
principalement utilisé sur les systèmes NeXTSTEP. Ce package n'inclue
pas la bibliothéque Objective C standard.

%description -l pl objc
Ten pakiet jest wsparciem obiektowego C dla kompilatora gcc. W
pakiecie nie ma jeszcze bibliotek C-obj.

%description -l tr objc
Bu paket, GNU C derleyicisine Objective C desteði ekler. Objective C,
C dilinin nesne yönelik bir türevidir ve NeXTSTEP altýnda çalýþan
sistemlerde yaygýn olarak kullanýlýr. Standart Objective C nesne
kitaplýðý bu pakette yer almaz.

%package g77
Summary:	Fortran 77 support for gcc
Summary(pl):	Wspomaganie Fortran 77 dla gcc
Group:		Development/Languages
Group(de):	Entwicklung/Sprachen
Group(pl):	Programowanie/Jêzyki
Obsoletes:	egcs-g77

%description g77
This apckage adds support for compiling Fortran 77 programs with the
GNU compiler.

%description -l pl g77
Ten pakiet jest wsparciem Fortran 77 dla kompilatora gcc. Jest
potrzebny do kompilowania programów pisanych w jêzyku Fortran 77.

%package chill
Summary:	CHILL support for gcc
Summary(pl):	Wspomoganie CHILL dla gcc
Group:		Development/Languages
Group(de):	Entwicklung/Sprachen
Group(pl):	Programowanie/Jêzyki
Requires:	%{name} = %{version}

%description chill
This package adds support for compiling CHILL programs with the GNU
compiler.

Chill is the "CCITT High-Level Language", where CCITT is the old name
for what is now ITU, the International Telecommunications Union. It is
is language in the Modula2 family, and targets many of the same
applications as Ada (especially large embedded systems). Chill was
never used much in the United States, but is still being used in
Europe, Brazil, Korea, and other places.

%package java
Summary:	Java support for gcc
Summary(pl):	Wspomoganie Java dla gcc
Group:		Development/Languages
Group(de):	Entwicklung/Sprachen
Group(pl):	Programowanie/Jêzyki
Requires:	%{name} = %{version}
Requires:	libgcj >= 2.95.1

%description java
This package adds experimental support for compiling Java(tm) programs
and bytecode into native code. To use this you will also need the
libgcj package.

%package -n libstdc++
Summary:	GNU c++ library
Summary(pl):	Biblioteki GNU C++ 
Group:		Libraries
Group(de):	Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Version:	%{STDC_VERSION}
Obsoletes:	libg++

%description -n libstdc++
This is the GNU implementation of the standard C++ libraries, along
with additional GNU tools. This package includes the shared libraries
necessary to run C++ applications.

%description -l de -n libstdc++
Dies ist die GNU-Implementierung der Standard-C++-Libraries mit
weiteren GNU-Tools. Dieses Paket enthält die zum Ausführen von
C++-Anwendungen erforderlichen gemeinsam genutzten Libraries.

%description -l fr -n libstdc++
Ceci est l'implémentation GNU des librairies C++ standard, ainsi que
des outils GNU supplémentaires. Ce package comprend les librairies
partagées nécessaires à l'exécution d'application C++.

%description -l pl -n libstdc++  
Pakiet ten zawiera biblioteki bêd±ce implementacj± standardowych
bibliotek C++. Znajduj± siê w nim biblioteki dynamiczne niezbêdne do
uruchomienia aplikacji napisanych w C++.

%description -l tr -n libstdc++
Bu paket, standart C++ kitaplýklarýnýn GNU gerçeklemesidir ve C++
uygulamalarýnýn koþturulmasý için gerekli kitaplýklarý içerir.

%package -n libstdc++-devel
Summary:	Header files and libraries for C++ development
Summary(de):	Header-Dateien und Libraries zur Entwicklung mit C++
Summary(fr):	Fichiers d'en-tête et biblitothèques pour développer en C++.
Summary(tr):	C++ ile program geliþtirmek için gerekli dosyalar
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Version:	%{STDC_VERSION}
Requires:	libstdc++ = %{STDC_VERSION}
Requires:	%{name}-c++
Obsoletes:	libg++-devel

%description -n libstdc++-devel
This is the GNU implementation of the standard C++ libraries. This
package includes the header files and libraries needed for C++
development.

%description -l pl -n libstdc++-devel
Pakiet ten zawiera biblioteki bêd±ce implementacj± standardowych
bibliotek C++. Znajduj± siê w nim pliki nag³ówkowe wykorzystywane przy
programowaniu w jêzyku C++.

%package -n libstdc++-static
Summary:	Static c++ standard library
Summary(pl):	Biblioeka statyczna c++
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Version:	%{STDC_VERSION}
Requires:	libstdc++-devel = %{STDC_VERSION}

%description -n libstdc++-static
Static c++ standard library.

%description -l pl -n libstdc++-static
Biblioteka statyczna C++.

%package -n cpp
Summary:	The C Pre Processor
Summary(pl):	Preprocesor C
Group:		Development/Languages
Group(de):	Entwicklung/Sprachen
Group(pl):	Programowanie/Jêzyki
Obsoletes:	egcs-cpp

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

%description -l pl -n cpp
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

%prep
%setup -q -n %{name}-%{ver}.test2
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p0
%patch5 -p0
#%patch6 -p1
%patch7 -p0
%patch8 -p0
#%patch9 -p0
%patch10 -p0
%patch11 -p0
%patch12 -p0
%patch13 -p1
#%ifarch arm
#%patch14 -p0
#%endif
%ifarch m68k
%patch15 -p0
%endif
%ifarch sparc sparc32
%patch16 -p0
%patch17 -p0
%patch18 -p1
%endif
%ifarch ppc
%patch19 -p0
%patch20 -p0
#%patch21 -p0
%endif
%ifarch alpha
%patch22 -p1
%endif
#%patch23 -p0
%patch24 -p0
%patch25 -p0
%patch26 -p0
#%patch27 -p1
#%patch28 -p1

%build
(cd gcc; autoconf)
rm -rf obj-%{_target_platform}
install -d obj-%{_target_platform} && cd obj-%{_target_platform} 

CFLAGS="%{?debug:-O -g}%{!?debug:$RPM_OPT_FLAGS}" \
CXXFLAGS="%{?debug:-O -g}%{!?debug:$RPM_OPT_FLAGS}" \
TEXCONFIG=false ../configure \
	--prefix=%{_prefix} \
	--infodir=%{_infodir} \
	--enable-shared \
%ifnarch sparc sparc64
	--enable-threads \
	--enable-haifa \
%endif
	--with-gnu-as \
	--with-gnu-ld \
	--with-gxx-include-dir="\$\{prefix\}/include/g++" \
	--disable-nls \
	%{_target_platform}

PATH=$PATH:/sbin:%{_sbindir}
touch  ../gcc/c-gperf.h

cd ..
%{__make} -C obj-%{_target_platform} bootstrap \
	LDFLAGS_FOR_TARGET="%{!?debug:-s}" \
	mandir=%{_mandir} \
	infodir=%{_infodir}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/lib,%{_datadir}}

cd obj-%{_target_platform}
PATH=$PATH:/sbin:%{_sbindir}

%{__make} install \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	mandir=$RPM_BUILD_ROOT%{_mandir} \
	infodir=$RPM_BUILD_ROOT%{_infodir}

%{__make} install \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	mandir=$RPM_BUILD_ROOT%{_mandir} \
	infodir=$RPM_BUILD_ROOT%{_infodir} -C texinfo

ln -sf gcc $RPM_BUILD_ROOT%{_bindir}/cc

echo .so g77.1 > $RPM_BUILD_ROOT%{_mandir}/man1/f77.1
echo .so cccp.1 > $RPM_BUILD_ROOT%{_mandir}/man1/cpp.1
install %{SOURCE1} $RPM_BUILD_ROOT%{_mandir}/man1/

ln -sf g77 $RPM_BUILD_ROOT%{_bindir}/f77
(cd $RPM_BUILD_ROOT%{_libdir} ; ln -sf libstdc++.so.*.*.* $RPM_BUILD_ROOT%{_libdir}/libstdc++.so)
ln -sf %{_bindir}/cpp $RPM_BUILD_ROOT/lib/cpp

gzip -9nf ../READ* ../ChangeLog ../gcc/ch/chill.brochure

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%post g77
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun g77
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%post chill
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun chill
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%post -n cpp
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun -n cpp
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

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
%{_mandir}/man1/gcov.1*
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
%attr(755,root,root) %{_bindir}/jv-scan

%attr(755,root,root) %{_libdir}/gcc-lib/%{_target_cpu}*/*/jc1
%attr(755,root,root) %{_libdir}/gcc-lib/%{_target_cpu}*/*/jvgenmain

%files -n libstdc++
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libstdc++.so.*.*.*

%files -n libstdc++-devel
%defattr(644,root,root,755)
%{_includedir}/g++
%attr(755,root,root) %{_libdir}/libstdc++.so

%files -n libstdc++-static
%defattr(644,root,root,755)
%attr(644,root,root) %{_libdir}/libstdc++.a

%files -n cpp
%defattr(644,root,root,755)
%attr(755,root,root) /lib/cpp
%attr(755,root,root) %{_bindir}/cpp
%attr(755,root,root) %{_libdir}/gcc-lib/%{_target_cpu}*/*/cpp0

%{_mandir}/man1/cpp.1*
%{_mandir}/man1/cccp.1*
%{_infodir}/cpp.info*.gz
