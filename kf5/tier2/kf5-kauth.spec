%define framework kauth

Name:           kf5-%{framework}
Version:        4.95.0
Release:        1%{?dist}
Summary:        KDE Frameworks 5 Tier 2 integration module to perform actions as privileged user

License:        GPLv2+
URL:            http://www.kde.org
Source0:        http://download.kde.org/unstable/frameworks/%{version}/%{framework}-%{version}.tar.xz

BuildRequires:  extra-cmake-modules
BuildRequires:  qt5-qtbase-devel

BuildRequires:  kf5-kcoreaddons-devel


%description
KAuth is a framework to let applications perform actions as a privileged user.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q -n %{framework}-%{version}

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
%doc COPYING.LIB README.md
%{_kf5_libdir}/libKF5Auth.so.*
%{_kf5_sysconfdir}/dbus-1/system.d/*
%{_kf5_plugindir}/plugins/kauth/
%{_kf5_datadir}/kauth/
%{_kf5_libexecdir}/kauth-policy-gen


%files devel
%{_kf5_includedir}/kauth_version.h
%{_kf5_includedir}/KAuth
%{_kf5_libdir}/libKF5Auth.so
%{_kf5_libdir}/cmake/KF5Auth


%changelog
* Thu Jan 09 2014 Daniel Vrátil <dvratil@redhat.com> 4.95.0-1
- Update to KDE Frameworks 5 TP1 (4.95.0)

* Sat Jan  4 2014 Daniel Vrátil <dvratil@redhat.com>
- initial version
