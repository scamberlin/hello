Name:           hello
Version:        1.0.13
Release:        1%{?dist}
Summary:        This is a test package

License:        BSD 
URL:            http://www.hello.com
Source0:        %{name}-%{version}.tar.gz

Requires:       coreutils
BuildRequires:  gcc
BuildRequires:  make

%description
This is a %{name} package.

%prep
%setup -q

%build
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
%make_install

%files
%doc
%{_bindir}/%{name}


%changelog
* Wed Dec 19 2018 stephane camberlin <stephane.camberlin@gmail.com> 1.0.13-1
- fix (stephane.camberlin@gmail.com)

* Wed Dec 19 2018 stephane camberlin <stephane.camberlin@gmail.com> 1.0.12-1
- cruel world (stephane.camberlin@gmail.com)

* Wed Dec 19 2018 stephane camberlin <stephane.camberlin@gmail.com> 1.0.11-1
- cruel world

* Wed Dec 19 2018 stephane camberlin <stephane.camberlin@gmail.com> 1.0.10-1
- test

* Wed Dec 19 2018 stephane camberlin <stephane.camberlin@gmail.com> 1.0.9-1
- 

* Wed Dec 19 2018 stephane camberlin <stephane.camberlin@gmail.com> 1.0.8-1
- fix version (stephane.camberlin@gmail.com)

* Wed Dec 19 2018 stephane camberlin <stephane.camberlin@gmail.com> 1.0.7-1
- add new test 

* Wed Dec 19 2018 stephane camberlin <stephane.camberlin@gmail.com> 1.0.6-1
- new test 

* Wed Dec 19 2018 stephane camberlin <stephane.camberlin@gmail.com> 1.0.5-1
- 

* Wed Dec 19 2018 stephane camberlin <stephane.camberlin@gmail.com> 1.0.4-1
- testing 

* Wed Dec 19 2018 stephane camberlin <stephane.camberlin@gmail.com> 1.0.3-1
- new package built with tito

* Wed Dec 19 2018 Stephane Camberlin <stephane.camberlin@gmail.com> 1.0.2-1
- test

* Wed Dec 19 2018 Stephane Camberlin <stephane.camberlin@gmail.com> 1.0.1-1
- new package built with tito
- in progress...

* Sun Dec 16 2018 Camberlin Stephane <stephane.camberlin@orange.com> - 1.0.0-1.fc29.sca
- first package
