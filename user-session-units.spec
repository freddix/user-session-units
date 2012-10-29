Summary:	Systemd units files related to user session
Name:		user-session-units
Version:	6
Release:	1
License:	GPL v3
Group:		Applications
Source0:	http://foo-projects.org/~sofar/user-session-units/%{name}-%{version}.tar.gz
# Source0-md5:	f7a48298eca6a32904fcf8900afc20b3
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	systemd-devel
BuildRequires:	pkg-config
BuildArch:	noarch
Requires:	dbus-launch
Requires:	systemd
Requires:	xorg-launch-helper
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains several systemd unit files related to the systemd
user session, aka `systemd --user`. The goal of this package is to
provide an easy way for people to collect, share and deploy systemd
user session installations and help test the systemd user session
core code.

%package xfce
Summary:	User session units for XFCE
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description xfce
User session units for XFCE.

%prep
%setup -q

sed -i -e "s|AC_ERROR|AC_WARNING|" configure.ac

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	XFCE_PROG="%{_bindir}/xfce4-session"	\
	XFWM_PROG="%{_bindir}/xfwm4"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
/usr/lib/systemd/system/shutdown.target.wants/systemd-stop-user-sessions.service
/usr/lib/systemd/system/systemd-stop-user-sessions.service
/usr/lib/systemd/system/user-session@.service
/usr/lib/systemd/user/dbus.service
/usr/lib/systemd/user/dbus.socket

%files xfce
%defattr(644,root,root,755)
%dir /usr/lib/systemd/user/xfce4.target.wants
/usr/lib/systemd/user/xfce4-session.service
/usr/lib/systemd/user/xfce4.target
/usr/lib/systemd/user/xfce4.target.wants/xfce4-session.service
/usr/lib/systemd/user/xfce4.target.wants/xfwm4.service
/usr/lib/systemd/user/xfwm4.service

