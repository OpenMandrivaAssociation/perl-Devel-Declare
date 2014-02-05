%define upstream_name    Devel-Declare
%define upstream_version 0.006015

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1
Epoch:		1

Summary:	Adding keywords to perl, in perl
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Devel/Devel-Declare-%{upstream_version}.tar.gz

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


%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1:0.6.5-2
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - update to new version 0.006005

* Sun May 08 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1:0.6.4-1
+ Revision: 672613
- update to new version 0.006004

* Thu Mar 10 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1:0.6.1-1
+ Revision: 643376
- update to new version 0.006001

  + Jérôme Quelin <jquelin@mandriva.org>
    - rebuild for perl 5.12
    - rebuild

* Tue Mar 09 2010 Jérôme Quelin <jquelin@mandriva.org> 1:0.6.0-1mdv2010.1
+ Revision: 517112
- update to 0.006000

* Mon Aug 17 2009 Jérôme Quelin <jquelin@mandriva.org> 1:0.5.11-1mdv2010.0
+ Revision: 417150
- adding missing buildrequires:
- update to 0.005011

* Tue Aug 11 2009 Jérôme Quelin <jquelin@mandriva.org> 1:0.5.9-1mdv2010.0
+ Revision: 415003
- bumping epoch
- update to 0.005009

* Wed Jul 15 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.005007-1mdv2010.0
+ Revision: 396217
- update to new version 0.005007

* Thu Jun 18 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.005006-1mdv2010.0
+ Revision: 387007
- update to new version 0.005006

* Sun Jun 07 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.005005-1mdv2010.0
+ Revision: 383477
- update to new version 0.005005

* Mon May 25 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.005003-1mdv2010.0
+ Revision: 379605
- update to new version 0.005003

* Mon May 11 2009 Jérôme Quelin <jquelin@mandriva.org> 0.005002-1mdv2010.0
+ Revision: 374550
- update to new version 0.005002

* Thu May 07 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.005001-1mdv2010.0
+ Revision: 373027
- update to new version 0.005001

* Fri May 01 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.005000-1mdv2010.0
+ Revision: 370050
- update to new version 0.005000

* Sun Dec 14 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.003004-1mdv2009.1
+ Revision: 314245
- update to new version 0.003004

* Wed Nov 26 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.003003-1mdv2009.1
+ Revision: 307111
- import perl-Devel-Declare


* Wed Nov 26 2008 cpan2dist 0.003003-1mdv
- initial mdv release, generated with cpan2dist



