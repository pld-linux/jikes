Summary:	A Java source file to bytecode compiler
Summary(es):	Compilador Java
Summary(pl):	Kompilator j�zyka Java
Summary(pt_BR):	Compilador Java
Name:		jikes
Version:	1.18
Release:	1
License:	IBM Public License Version 1.0 - Jikes Compiler, http://ibm.com/research/jikes/license/license3.htm
Group:		Development/Languages/Java
Source0:	ftp://www-126.ibm.com/pub/%{name}/%{version}/%{name}-%{version}.tar.bz2
Patch0:		%{name}-NAN.patch
URL:		http://oss.software.ibm.com/developerworks/opensource/jikes/
BuildRequires:	libstdc++-devel
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
development model.

%description -l es
Jikes (TM) es un compilador de fuentes Java para bytecode. Es un
compilador r�pido y que sigue estrictamente los patrones del lenguaje
Java.

%description -l pl
Jikes z IBM Research to kompilator t�umacz�cy pliki �r�d�owe Javy na
bytecode. Jikes jest �ci�le zgodny ze specyfikacj� j�zyka, ma bardzo
du�� szybko�� kompilacji i przemy�lan� analiz� zale�no�ci pozwalaj�c�
n przyrostow� kompilacj� i automatyczne generowanie makefile.

%description -l pt_BR
Jikes (TM) � um compilador de fontes Java para bytecode. � um
compilador r�pido e que segue estritamente os padr�es da linguagem
Java.

%prep
%setup -q
#%patch0 -p1

%build
CXXFLAGS="%{rpmcflags} -fno-exceptions -fno-rtti"
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/jikes
%{_mandir}/man1/jikes.1*
