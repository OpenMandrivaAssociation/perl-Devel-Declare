%define upstream_name    Devel-Declare
%define upstream_version 0.006016

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3
Epoch:		1

Summary:	Adding keywords to perl, in perl

License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Devel/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(B::Compiling)
BuildRequires: perl(Module::Implementation)
BuildRequires: perl(Test::Requires)
BuildRequires:	perl(B::Hooks::EndOfScope)
BuildRequires:	perl(B::Hooks::OP::Check)
BuildRequires:	perl(ExtUtils::Depends)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(Sub::Name)
BuildRequires:	perl(Test::More) >= 0.880.0
BuildRequires:	perl(Test::Warn)
BuildRequires:	perl-devel

%description
Devel::Declare can install subroutines called declarators which locally
take over Perl's parser, allowing the creation of new syntax.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorarch}/Devel
%{perl_vendorarch}/auto/Devel



