Name:           hello
Version:        1.0.4
Release:        1%{?dist}
Summary:        This is a test package

License:        BSD 
URL:            http://www.hello.com
Source0:        hello-1.0.0.tar.gz

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
