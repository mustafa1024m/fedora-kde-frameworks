#%define snapshot 20140205
%define framework karchive

Name:           kf5-%{framework}
Version:        4.98.0
Release:        1.20140418gitc764b839%{?dist}
Summary:        KDE Frameworks 5 Tier 1 addon with archive functions

License:        GPLv2+
URL:            http://www.kde.org

# git archive --format=tar --prefix=%{framework}-%{version}/ \
#             --remote=git://anongit.kde.org/%{framework}.git master | \
# bzip2 -c > %{name}-%{version}-%{snapshot}git.tar.bz2
#Source0:        %{name}-%{version}-%{snapshot}git.tar.bz2
Source0:        kf5-karchive-c764b839.tar

BuildRequires:  zlib-devel
BuildRequires:  bzip2-devel
BuildRequires:  lzma-devel

BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  qt5-qtbase-devel

Requires:       kf5-filesystem

%description
KDE Frameworks 5 Tier 1 addon with archive functions


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

make %{?_smp_mflags} -C %{_target_platform}

%install
%make_install -C %{_target_platform}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%doc AUTHORS COPYING COPYING.LIB INSTALL README.md
%{_kf5_libdir}/libKF5Archive.so.*

%files devel
%{_kf5_includedir}/karchive_version.h
%{_kf5_includedir}/KArchive
%{_kf5_libdir}/libKF5Archive.so
%{_kf5_libdir}/cmake/KF5Archive
%{_kf5_archdatadir}/mkspecs/modules/qt_KArchive.pri

%changelog
* Fri Apr 18 2014 dvratil <dvratil@redhat.com> - 4.98.0-20140418gitc764b839
- Update to git: c764b839

* Mon Mar 31 2014 Jan Grulich <jgrulich@redhat.com> 4.98.0-1
- Update to KDE Frameworks 5 Beta 1 (4.98.0)

* Wed Mar 05 2014 Jan Grulich <jgrulich@redhat.com> 4.97.0-1
- Update to KDE Frameworks 5 Alpha 1 (4.97.0)

* Wed Feb 12 2014 Daniel Vrátil <dvratil@redhat.com> 4.96.0-1
- Update to KDE Frameworks 5 Alpha 1 (4.96.0)

* Wed Feb 05 2014 Daniel Vrátil <dvratil@redhat.com> 4.96.0-0.1.20140205git
- Update to pre-release snapshot of 4.96.0

* Thu Jan 09 2014 Daniel Vrátil <dvratil@redhat.com> 4.95.0-1
- Update to KDE Frameworks 5 TP1 (4.95.0)

* Sat Jan  4 2014 Daniel Vrátil <dvratil@redhat.com>
- initial version