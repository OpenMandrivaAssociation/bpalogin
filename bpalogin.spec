%define name bpalogin
%define version 2.0.2
%define release %mkrel 7

Summary: Client for Telstra's Big Pond Advance cable connections
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://bpalogin.sourceforge.net/download/%{name}-%{version}.tar.bz2
Patch0: bpalogin-2.0.2-fix-str-fmt.patch
License: GPL
Group: System/Servers
Url: http://bpalogin.sourceforge.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires(post): rpm-helper
Requires(preun): rpm-helper


%description
BPALogin is a replacement for the Telstra supplied client for
connecting and using Telstra's Big Pond Advance powered by Cable. The
current implementation was written by Shane Hyde, but is now being
maintained by William Rose and others based at SourceForge.

%prep
%setup -q
%patch0 -p0

%build
%serverbuild
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%post
%_post_service %{name}

%preun
%_preun_service  %{name}

%files
%defattr(-,root,root)
%doc COPYING CREDITS INSTALL README 
%config(noreplace) %{_sysconfdir}/%{name}.conf
%attr(755,root,root) %{_initrddir}/%{name}
%{_sbindir}/%{name}

