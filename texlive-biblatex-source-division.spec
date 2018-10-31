# revision 34267
# category Package
# catalog-ctan /macros/latex/contrib/biblatex-contrib/biblatex-source-division
# catalog-date 2014-06-17 21:28:47 +0200
# catalog-license lppl1.3
# catalog-version 2.2.0
Name:		texlive-biblatex-source-division
Version:	2.4.2
Release:	2
Summary:	References by "division" in classical sources
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-contrib/biblatex-source-division
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-source-division.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-source-division.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
