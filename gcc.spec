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
BuildRoot:	/tmp/%{name}-%{version}-root
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
	--gxx-include-dir=%{_includedir}/g++ \
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
ln -sf gcc $RPM_BUILD_ROOT%{_bindir}/cc
rm -rf $RPM_BUILD_ROOT%{_libdir}/gcc-lib/${RPM_ARCH}/*/include/objc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS PROBLEMS
%attr(755,root,root) %{_bindir}/*-linux-gcc
%dir %{_libdir}/gcc-lib/*/*
%dir %{_libdir}/gcc-lib/*/*/include
%{_libdir}/gcc-lib/*/*/SYSCALLS.c.X
%attr(755,root,root) %{_libdir}/gcc-lib/*/*/cc1
%attr(755,root,root) %{_libdir}/gcc-lib/*/*/cpp
%{_libdir}/gcc-lib/*/*/libgcc.a
%{_libdir}/gcc-lib/*/*/specs
%{_libdir}/gcc-lib/*/*/include/*
%{_libdir}/gcc-lib/*/*/*.o
