%define snapshot  20140104

Name:           kf5-kservice
Version:        5.0.0
Release:        0.1.%{snapshot}git
Summary:        KDE Frameworks tier 3 solution for working with .desktop files

License:        GPLv2+
URL:            http://www.kde.org

# git archive --format=tar --prefix=%{name}-%{snapshot}/ \
#             --remote=git://anongit.kde.org/%{name}-framework.git master | \
# gzip -c > %{name}-framework-%{snapshot}.tar.gz
Source0:        %{name}-%{snapshot}.tar.gz

BuildRequires:  extra-cmake-modules
BuildRequires:  qt5-qtbase-devel
BuildRequires:  kf5-kconfig-devel
BuildRequires:  kf5-kcoreaddons-devel
BuildRequires:  kf5-kcrash-devel
BuildRequires:  kf5-kdbusaddons-devel
BuildRequires:  kf5-ki18n-devel
BuildRequires:  kf5-kjs-devel
BuildRequires:  kf5-kdoctools-devel
BuildRequires:  kf5-kwindowsystem-devel
BuildRequires:  kf5-karchive-devel


%description
KDE Frameworks tier 3 solution for working with .desktop files


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q


%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd

make %{?_smp_mflags} DESTDIR=%{buildroot} -C %{_target_platform}

%install
%make_install -C %{_target_platform}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%doc COPYING COPYING.LIB README.md
%{_kf5_libdir}/*.so.*
%{_kf5_bindir}/*
%{_kf5_sysconfdir}/xdg/menus/applications.menu
%{_kf5_datadir}/kde5/servicetypes/*.desktop
%{_kf5_mandir}/man8/*

%files devel
%doc
%{_kf5_includedir}/*
%{_kf5_libdir}/*.so
%{_kf5_libdir}/cmake/KF5Service


%changelog
* Sat Jan  4 2014 Daniel Vrátil <dvratil@redhat.com>
- initial version
