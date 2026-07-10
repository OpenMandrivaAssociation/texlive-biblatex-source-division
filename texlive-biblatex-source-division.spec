%global tl_name biblatex-source-division
%global tl_revision 76790

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.4.2
Release:	%{tl_revision}.1
Summary:	References by division in classical sources
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-contrib/biblatex-source-division
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-source-division.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-source-division.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package enables the user to make reference to "division marks" (such
as book, chapter, section), in the document being referenced, in
addition to the page-based references that BibTeX-based citations have
always had. The citation is made in the same way as the LaTeX standard,
but what's inside the square brackets may include the "division"
specification, as in \cite[(<division spec.>)<page number>]{<document>}

