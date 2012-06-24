Summary:	A Java source file to bytecode compiler
Summary(es.UTF-8):	Compilador Java
Summary(pl.UTF-8):	Kompilator języka Java do bajtkodu
Summary(pt_BR.UTF-8):	Compilador Java
Name:		jikes
Version:	1.22
Release:	3
License:	IBM Public License Version 1.0 - Jikes Compiler, http://ibm.com/research/jikes/license/license3.htm
Group:		Development/Languages/Java
Source0:	http://dl.sourceforge.net/jikes/%{name}-%{version}.tar.bz2
# Source0-md5:	cda958c7fef6b43b803e1d1ef9afcb85
Patch0:		%{name}-source-1.2.patch
URL:		http://jikes.sourceforge.net/
BuildRequires:	automake
BuildRequires:	libstdc++-devel
Obsoletes:	guavac
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
development model.

%description -l es.UTF-8
Jikes (TM) es un compilador de fuentes Java para bytecode. Es un
compilador rápido y que sigue estrictamente los patrones del lenguaje
Java.

%description -l pl.UTF-8
Jikes z IBM Research to kompilator tłumaczący pliki źródłowe Javy do
bajtkodu. Jikes jest ściśle zgodny ze specyfikacją języka, ma bardzo
dużą szybkość kompilacji i przemyślaną analizę zależności pozwalającą
na przyrostową kompilację i automatyczne generowanie skryptów dla
programu GNU Make.

%description -l pt_BR.UTF-8
Jikes (TM) é um compilador de fontes Java para bytecode. É um
compilador rápido e que segue estritamente os padrões da linguagem
Java.

%prep
%setup -q
%patch0 -p1

%build
cp -f /usr/share/automake/config.sub .

%configure \
	--enable-source15
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO doc/license.htm
%attr(755,root,root) %{_bindir}/jikes
%{_includedir}/jikesapi.h
%{_mandir}/man1/jikes.1*
