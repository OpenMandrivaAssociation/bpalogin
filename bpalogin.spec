Summary:	Client for Telstra's Big Pond Advance cable connections
Name:		bpalogin
Version:	2.0.2
Release:	22
License:	GPLv2
Group:		System/Servers
Url:		http://bpalogin.sourceforge.net/
Source0:	http://bpalogin.sourceforge.net/download/%{name}-%{version}.tar.bz2
Patch0:		bpalogin-2.0.2-fix-str-fmt.patch
Requires(post,preun):	rpm-helper

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
%makeinstall_std

%post
%_post_service %{name}

%preun
%_preun_service  %{name}

%files
%doc COPYING CREDITS INSTALL README 
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_initrddir}/%{name}
%{_sbindir}/%{name}

