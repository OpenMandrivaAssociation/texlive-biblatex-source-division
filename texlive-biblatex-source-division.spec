Name:		texlive-biblatex-source-division
Version:	45379
Release:	1
Summary:	References by "division" in classical sources
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-contrib/biblatex-source-division
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-source-division.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-source-division.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package enables the user to make reference to "division
marks" (such as book, chapter, section), in the document being
referenced, in addition to the page-based references that
BibTeX-based citations have always had. The citation is made in
the same way as the LaTeX standard, but what's inside the
square brackets may include the "division" specification, as in
\cite[<division spec.>]{<document>}.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/biblatex-source-division/biblatex-source-division.sty
%doc %{_texmfdistdir}/doc/latex/biblatex-source-division/README
%doc %{_texmfdistdir}/doc/latex/biblatex-source-division/biblatex-source-division.bib
%doc %{_texmfdistdir}/doc/latex/biblatex-source-division/biblatex-source-division.pdf
%doc %{_texmfdistdir}/doc/latex/biblatex-source-division/biblatex-source-division.tex
%doc %{_texmfdistdir}/doc/latex/biblatex-source-division/latexmkrc
%doc %{_texmfdistdir}/doc/latex/biblatex-source-division/makefile

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
