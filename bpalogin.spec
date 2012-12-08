%define name bpalogin
%define version 2.0.2
%define release %mkrel 12

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



%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 2.0.2-10mdv2011.0
+ Revision: 663336
- mass rebuild

* Tue Nov 30 2010 Oden Eriksson <oeriksson@mandriva.com> 2.0.2-9mdv2011.0
+ Revision: 603769
- rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 2.0.2-8mdv2010.1
+ Revision: 522301
- rebuilt for 2010.1

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 2.0.2-7mdv2010.0
+ Revision: 413184
- rebuild

* Tue Apr 07 2009 Funda Wang <fwang@mandriva.org> 2.0.2-6mdv2009.1
+ Revision: 364738
- fix  str fmt
- use server flags

* Mon Jun 16 2008 Thierry Vignaud <tv@mandriva.org> 2.0.2-6mdv2009.0
+ Revision: 220492
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 2.0.2-5mdv2008.1
+ Revision: 136280
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Fri May 12 2006 Stefan van der Eijk <stefan@eijk.nu> 2.0.2-5mdk
- rebuild for sparc

* Sat Dec 31 2005 Mandriva Linux Team <http://www.mandrivaexpert.com/> 2.0.2-4mdk
- Rebuild

* Thu Aug 11 2005 Nicolas Lécureuil <neoclust@mandriva.org> 2.0.2-3mdk
- fix rpmlint errors (PreReq

* Thu Aug 11 2005 Nicolas Lécureuil <neoclust@mandriva.org> 2.0.2-2mdk
- fix rpmlint errors (PreReq)

* Mon Jan 31 2005 Olivier Blin <blino@mandrake.org> 2.0.2-1mdk
- initial Mandrakelinux release

