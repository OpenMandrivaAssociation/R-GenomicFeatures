%bcond_with internet
%global packname  GenomicFeatures
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.6.8
Release:          2
Summary:          Tools for making and manipulating transcript centric annotations
Group:            Sciences/Mathematics
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
Requires:         R-IRanges R-GenomicRanges R-AnnotationDbi R-methods R-DBI
Requires:         R-RSQLite R-Biostrings R-rtracklayer R-biomaRt R-RCurl
Requires:         R-utils R-Biobase R-org.Mm.eg.db R-BSgenome
Requires:         R-BSgenome.Hsapiens.UCSC.hg18 R-BSgenome.Celegans.UCSC.ce2
Requires:         R-RUnit
BuildRequires:    R-devel Rmath-devel texlive-collection-latex
BuildRequires:    R-IRanges R-GenomicRanges R-AnnotationDbi R-methods R-DBI
BuildRequires:    R-RSQLite R-Biostrings R-rtracklayer R-biomaRt R-RCurl
BuildRequires:    R-utils R-Biobase R-org.Mm.eg.db R-BSgenome
BuildRequires:    R-BSgenome.Hsapiens.UCSC.hg18 R-BSgenome.Celegans.UCSC.ce2
BuildRequires:    R-RUnit 

%description
A set of tools and methods for making and manipulating transcript centric
annotations. With these tools the user can easily download the genomic
locations of the transcripts, exons and cds of a given organism, from
either the UCSC Genome Browser or a BioMart database (more sources will be
supported in the future). This information is then stored in a local
database that keeps track of the relationship between transcripts, exons,
cds and genes. Flexible methods are provided for extracting the desired
features in a convenient format.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%if %{with internet}
%check
%{_bindir}/R CMD check %{packname}
%endif

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/txdb-template
%{rlibdir}/%{packname}/unitTests
