Name:           khelpcenter
Version:        5.0.0
Release:        1%{?dist}
Summary:        Application to show KDE Application's documentation

License:        GPLv2+
URL:            http://www.kde.org

Source0:        http://download.kde.org/stable/plasma/%{version}/%{name}-%{version}.tar.xz

BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtscript-devel

BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules

BuildRequires:  kf5-kconfig-devel
BuildRequires:  kf5-kinit-devel
BuildRequires:  kf5-kcmutils-devel
BuildRequires:  kf5-khtml-devel
BuildRequires:  kf5-kdelibs4support-devel
BuildRequires:  kf5-kdoctools-devel

Requires:       kf5-filesystem

Obsoletes:      kde-runtime-khelpcenter < 5.0.0-1

%description
An advanced editor component which is used in numerous KDE applications
requiring a text editing component.

%prep
%setup -q

%build

sed -e "s/PO_FILES //" -i po/*/CMakeLists.txt

mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd

make %{?_smp_mflags} -C %{_target_platform}

%install
%make_install -C %{_target_platform}
%find_lang khelpcenter5 --with-qt --all-name

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f khelpcenter5.lang
%doc README.htdig README.metadata COPYING
%{_bindir}/khelpcenter
%{_libexecdir}/khc_indexbuilder
%{_libexecdir}/khc_htdig.pl
%{_libexecdir}/khc_htsearch.pl
%{_libexecdir}/khc_mansearch.pl
%{_libexecdir}/khc_docbookdig.pl
%{_kf5_libdir}/libkdeinit5_khelpcenter.so
%{_kf5_datadir}/khelpcenter
%{_datadir}/applications/Help.desktop
%{_datadir}/config.kcfg/khelpcenter.kcfg
%{_datadir}/kservices5/khelpcenter.desktop
%{_datadir}/dbus-1/interfaces/org.kde.khelpcenter.kcmhelpcenter.xml
%{_datadir}/doc/HTML/en/khelpcenter
%{_datadir}/doc/HTML/en/fundamentals
%{_datadir}/doc/HTML/en/onlinehelp

%changelog
* Wed Jul 16 2014 Daniel Vrátil <dvratil@redhat.com> - 5.0.0-1
- Plasma 5.0.0

* Wed May 14 2014 Daniel Vrátil <dvratil@redhat.com> - 4.90.1-1.20140514git6bfae0d
- Intial snapshot
