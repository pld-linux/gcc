Summary:     GNU C Compiler
Summary(de): GNU-C-Compiler 
Summary(fr): Compilateur C de GNU
Summary(pl): Kompilator GNU C
Summary(tr): GNU C derleyicisi
Name:        gcc
Version:     2.7.2.3
Release:     16
Copyright:   GPL
Group:       Development/Languages
Source:      ftp://prep.ai.mit.edu/pub/gnu/%{name}-%{version}.tar.gz
Patch1:      gcc-2.7.2-make.patch
Patch2:      gcc-2.7.2.sparc.patch
Patch3:      ftp://atheist.tamu.edu/pub/richard/linux/axp/rth-gcc-2.7.2-960814.diff.gz
Patch4:      gcc-2.7.2-pg.patch
Patch5:      gcc-2.7.2-flow.patch
Patch6:      ftp://ftp.redhat.com/pub/alphabits/rth-gcc-2.7.2-961121.diff.gz
Patch7:      gcc-2.7.2.sparc.patch2
Patch8:      gcc-2.7.2.3-glibc2.patch
Patch9:      gcc-2.7.2-alpha-ra.patch
Requires:    binutils
Prereq:      /sbin/install-info
Buildroot:   /tmp/%{name}-%{version}-root
Exclusivearch: i386

%description
The GNU C compiler -- a full featured ANSI C compiler, with support
for K&R C as well. GCC provides many levels of source code error
checking tradionaly provided by other tools (such as lint), produces
debugging information, and can perform many different optimizations to
the resulting object code.

%description -l de
Der GNU-C-Compiler, ein ANSI-C-Compiler mit komplettem Funktions-
umfang sowie Unterstützung für K&R. GCC bietet viele Ebenen der
Quell-Code-Fehlerprüfung, wie sie früher durch separate Tools bereitgestellt
wurde (etwa lint), produziert Debug-Infos und ist in der Lage, viele
verschiedene Optimierungen am resultierenden Objektcode auszuführen. 

%description -l fr
Le compilateur C GNU -- un compilateur C ANSI complet, avec un support
pour la norme K&R. GCC fournit de nombreux niveaux d'erreurs donnés par
des outils extérieurs (comme lint), produit des informations de débogage,
et peut réaliser différentes optimisations sur le code objet produit.

%description -l pl
Kompilator GNU C jest pe³nowartosciowym kompilatorem ANSI C akceptuj±cym
tak¿e K&R C. GCC udostêpnia wielopoziomowe sprawdzanie i raportowanie
b³êdów na poziomie kodu ¼ród³owego w C jakie udostêpniaj± inne narzêdzia jak
np. lint. GCC Umo¿liwia tak¿e wygenerowanie kodu wynikowego z informacjami
do debugera, a tak¿e umo¿liwia generowanie zoptymalizowanego kodu
wynikowego.

%description -l tr
GNU C derleyicisi, K&R C desteði olan ve ANSI C'nin bütün özelliklerine sahip
bir derleyicidir. Normalde baþka araçlarýn (örneðin lint) yaptýðý kaynak kodu
düzeyindeki pek çok hata denetimini gerçekleþtirir, hata ayýklama bilgisi
üretebilir ve sonuç olarak ortaya çýkan ara kod üzerinde birçok optimizasyon
uygulayabilir.

%prep
%setup -q
%patch1 -p1 -b .rh

%ifarch sparc alpha
%patch2 -p1
%patch3 -p1
%patch4 -p0
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1 -b .glibc2
%patch9 -p0 -b .alphara
%endif

%build
./configure \
	--prefix=/usr \
	--local-prefix=/usr/local \
	--gxx-include-dir=/usr/include/g++ \
	--host=%{_target_cpu}-linux \
	--target=%{_target_cpu}-linux

make LANGUAGES=c CFLAGS="-O2"
make stage1
make CC="stage1/xgcc -Bstage1/" CFLAGS="-O2" LDFLAGS="-s"
make stage2
make CC="stage2/xgcc -Bstage2/" CFLAGS="-O2" LDFLAGS="-s"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/{bin,lib,info,man}
make CC="stage2/xgcc -Bstage2/" CFLAGS="-O2" LDFLAGS="-s" install \
	prefix=$RPM_BUILD_ROOT/usr

gzip -n -9f $RPM_BUILD_ROOT%{_infodir}/gcc.info*
ln -sf gcc $RPM_BUILD_ROOT/usr/bin/cc
rm -rf $RPM_BUILD_ROOT/usr/lib/gcc-lib/${RPM_ARCH}/*/include/objc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)
%doc NEWS PROBLEMS
%attr(755, root, root) /usr/bin/*-linux-gcc
%dir /usr/lib/gcc-lib/*/*
%dir /usr/lib/gcc-lib/*/*/include
/usr/lib/gcc-lib/*/*/SYSCALLS.c.X
%attr(755, root, root) /usr/lib/gcc-lib/*/*/cc1
%attr(755, root, root) /usr/lib/gcc-lib/*/*/cpp
/usr/lib/gcc-lib/*/*/libgcc.a
/usr/lib/gcc-lib/*/*/specs
/usr/lib/gcc-lib/*/*/include/*
/usr/lib/gcc-lib/*/*/*.o

%changelog
* Mon Nov 16 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [2.7.2.3-16]
- now gcc 2.7.2.3 for backward compatybility for proper
  compiling kernel 2.0.x is compiled like cross compilator
  (remember use "CC=<arch>-linux-gcc" as make parameter during
  compile kernel),
- removed gcc man and inbfo page (this can be provided by egcs).

* Sun Sep 27 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [2.7.2.3-15]
- added full %attr description in %files,
- fiew simplifications in %install and %files.

* Wed Sep  2 1998 Jeff Johnson <jbj@redhat.com>
- eliminate gcc on sparc in RH5.2; sparclinux-2.0-980805 works with egcs.

* Mon Jul 13 1998 Jeff Johnson <jbj@redhat.com>
- sparc gets gcc/cc from egcs. someday ((after RH-5.2) i386 will too.

* Wed Jul  8 1998 Jeff Johnson <jbj@redhat.com>
- resurrect gcc for sparc kernel compiles.

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Apr 30 1998 Cristian Gafton <gafton@redhat.com>
- use extensively CFLAGS="-O2" when building the compiler (this is known to
  help the fully compatible Cyrix chips (sic!) to run this beast)

* Mon Apr 20 1998 Cristian Gafton <gafton@redhat.com>
- better yet, ExclusiveArch: i386 is in effect

* Tue Apr 14 1998 Cristian Gafton <gafton@redhat.com>
- removed the c++ package as we are swhiching to egcs-c++
- idem for objc
- added buildroot
- alpha is exlcuded from the build. I don't know about sparc yet, so I leave
  it for this time

* Fri Oct 23 1997 Erik Troan <ewt@redhat.com>
- use ld-linux.so.2 on the sparc

* Fri Oct 10 1997 Erik Troan <ewt@redhat.com>
- build crtbegin* and crtend* on the sparc

* Mon Sep 29 1997 Erik Troan <ewt@redhat.com>
- added patch from rth to fix dump on alpha w/ building libg++

* Sun Sep 28 1997 Erik Troan <ewt@redhat.com>
- djb really made the crtbegin/end stuff in gcc-c-skel conditional on
  running on an i386 machine, not a !sparc machine; all changed was his
  comment
- added patch to use /lib/ld-linux.so.2 on the alpha

* Tue Sep 23 1997 Richard Henderson <rth@cygnus.com>
- Killed the glibc.patch and added sparc.patch2 to _really_ make
  libgcc.a be compiled with -fPIC.

* Fri Sep 19 1997 Donald Barnes <djb@redhat.com>
- added the glibc.patch so that libgcc.a is compiled with -fPIC
- added %ifarch i386 around crtbegin/end in gcc-c-skel

* Sun Sep 14 1997 Erik Troan <ewt@redhat.com>
- modified to use install-info

* Sun Aug 24 1997 Erik Troan <ewt@redhat.com>
- updated to gcc 2.7.2.3

* Thu Aug 21 1997 Erik Troan <ewt@redhat.com>
- fixed /lib/cpp patch to include redhat element

* Mon Jun 02 1997 Erik Troan <ewt@redhat.com>
- removed HJ's patch
- added patch from Ulrich Drepper to generate crt*.o
