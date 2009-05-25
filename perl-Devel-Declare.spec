%define module   Devel-Declare
%define version    0.005003
%define release    %mkrel 1

Name:       perl-%{module}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Adding keywords to perl, in perl
Url:        http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/Devel/%{module}-%{version}.tar.gz
BuildRequires: perl-devel
BuildRequires: perl(B::Hooks::EndOfScope)
BuildRequires: perl(B::Hooks::OP::Check)
BuildRequires: perl(ExtUtils::Depends)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Sub::Name)
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
setup_for
      Devel::Declare->setup_for(
        $package,
        {
          $name => { $op_type => $sub }
        }
      );

    Currently valid op types: 'check', 'rv2cv'



%prep
%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorarch/Devel
%perl_vendorarch/auto/Devel


