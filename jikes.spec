Summary:	A Java source file to bytecode compiler.
Summary(pl):	Kompilator jêzyka Java.
Name:		jikes
Version:	1.12
Release:	2
Copyright:	IBM Public License Version 1.0 - Jikes Compiler, http://ibm.com/research/jikes/license/license3.htm
Group:		Development/Languages
Url:		http://OSS.Software.IBM.Com/developerworks/opensource/jikes/project/
Source0:	http://OSS.Software.IBM.Com/developerworks/opensource/jikes/project/pub/%{name}-%{version}.tar.gz
Patch0:		jikes-gccbug.patch
Patch1:		jikes-gcc296.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

#%description -l pl
#N/A

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} bindir=$RPM_BUILD_ROOT%{_bindir} mandir=$RPM_BUILD_ROOT%{_mandir} install -C src
install -d $RPM_BUILD_ROOT%{_mandir}/man1
install doc/jikes.1 $RPM_BUILD_ROOT%{_mandir}/man1
gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/*
gzip -9nf README doc/{contrib.html,jikes.html,license.htm,news.html}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,doc/{contrib.html,jikes.html,license.htm,news.html}}.gz
%{_mandir}/man1/jikes.1*
%attr(755, root, root) %{_bindir}/jikes
