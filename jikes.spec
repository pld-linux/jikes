Summary:	A Java source file to bytecode compiler
Summary(pl):	Kompilator jêzyka Java
Name:		jikes
Version:	1.13
Release:	1
License:	IBM Public License Version 1.0 - Jikes Compiler, http://ibm.com/research/jikes/license/license3.htm
Group:		Development/Languages
Group(de):	Entwicklung/Sprachen
Group(pl):	Programowanie/Jêzyki
Source0:	http://oss.software.ibm.com/pub/jikes/%{name}-%{version}.tar.gz
URL:		http://oss.software.ibm.com/developerworks/opensource/jikes/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	guavac

%description
The IBM Research Jikes compiler translates Java source files into
bytecode. Jikes' features include strict adherence to the language
specification, extremely fast compile speed, and a sophisticated
dependence analysis that allows for incremental compilation and
automatic makefile generation.

The release of Jikes' source code in December 1998 initiated one of
IBM's first efforts in the open source arena, and since that time
Jikes has been maintained and refined using the open source
development model. See http://ibm.com/research/jikes for more
information.

%prep
%setup -q

%build
CXXFLAGS="%{?debug:-O0 -g}%{!?debug:$RPM_OPT_FLAGS} -fno-exceptions -fno-rtti"
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/man1

%{__make} install -C src \
	bindir=$RPM_BUILD_ROOT%{_bindir} \
	mandir=$RPM_BUILD_ROOT%{_mandir}

install doc/jikes.1 $RPM_BUILD_ROOT%{_mandir}/man1

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz doc/*.html
%attr(755,root,root) %{_bindir}/jikes
%{_mandir}/man1/jikes.1*
