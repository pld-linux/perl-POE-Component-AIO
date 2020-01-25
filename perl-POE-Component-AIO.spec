#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	POE
%define	pnam	Component-AIO
Summary:	POE::Component::AIO - Asynchronous Input/Output for POE
#Summary(pl.UTF-8):	
Name:		perl-POE-Component-AIO
Version:	1.00
Release:	1
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/POE/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	27449af8deb647f17be209abe2e9e9e8
URL:		http://search.cpan.org/dist/POE-Component-AIO/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-IO-AIO
BuildRequires:	perl-POE
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This component adds support for IO::AIO use in POE

# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/POE/Component/*.pm
#%%{perl_vendorlib}/POE/Component/AIO
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
