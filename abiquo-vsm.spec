%define abiquo_basedir /opt/abiquo

Name:     abiquo-vsm
Version: 1.7
Release: 2%{?dist}%{?buildstamp}
Summary:  Abiquo Virtual System Monitor
Group:    Development/System 
License:  Multiple 
URL:      http://www.abiquo.com 
Source0:  %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: abiquo-core

%description
Next Generation Cloud Management Solution

This package contains the enterprise vsm component.

This package includes software developed by third-party.
Make sure that you read the license agrements in /usr/share/doc/abiquo-core licenses before using this software.


%prep
%setup -q

%build


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{abiquo_basedir}/tomcat/webapps/
mkdir -p $RPM_BUILD_ROOT/%{_docdir}/%{name}
cp -r . $RPM_BUILD_ROOT/%{abiquo_basedir}/tomcat/webapps/vsm


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{abiquo_basedir}/tomcat/webapps/vsm

%changelog
* Tue Dec 14 2010 Sergio Rubio <srubio@abiquo.com> - 1.7-2
- use the new build system

* Mon Nov 22 2010 Sergio Rubio <srubio@abiquo.com> 1.7-1
- Updated to upstream 1.7

* Tue Oct 05 2010 Sergio Rubio <srubio@abiquo.com> 1.6.8-1
- Updated to upstream 1.6.8

* Thu Sep 02 2010 Sergio Rubio srubio@abiquo.com 1.6.5-1
- updated to 1.6.5

* Fri Jul 09 2010 Sergio Rubio srubio@abiquo.com 1.6-2
- Added buildstamp to the package

* Mon Jul 05 2010 Sergio Rubio srubio@abiquo.com 1.6-1
- Updated to upstream 1.6

* Wed May 26 2010 Sergio Rubio srubio@abiquo.com 1.5.1
- Initial Release
