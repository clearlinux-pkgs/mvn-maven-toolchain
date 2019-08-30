#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-maven-toolchain
Version  : 2.2.1
Release  : 3
URL      : https://repo1.maven.org/maven2/org/apache/maven/maven-toolchain/2.2.1/maven-toolchain-2.2.1.jar
Source0  : https://repo1.maven.org/maven2/org/apache/maven/maven-toolchain/2.2.1/maven-toolchain-2.2.1.jar
Source1  : https://repo1.maven.org/maven2/org/apache/maven/maven-toolchain/1.0/maven-toolchain-1.0.jar
Source2  : https://repo1.maven.org/maven2/org/apache/maven/maven-toolchain/1.0/maven-toolchain-1.0.pom
Source3  : https://repo1.maven.org/maven2/org/apache/maven/maven-toolchain/2.0.9/maven-toolchain-2.0.9.jar
Source4  : https://repo1.maven.org/maven2/org/apache/maven/maven-toolchain/2.0.9/maven-toolchain-2.0.9.pom
Source5  : https://repo1.maven.org/maven2/org/apache/maven/maven-toolchain/2.1.0/maven-toolchain-2.1.0.jar
Source6  : https://repo1.maven.org/maven2/org/apache/maven/maven-toolchain/2.1.0/maven-toolchain-2.1.0.pom
Source7  : https://repo1.maven.org/maven2/org/apache/maven/maven-toolchain/2.2.1/maven-toolchain-2.2.1.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-maven-toolchain-data = %{version}-%{release}
Requires: mvn-maven-toolchain-license = %{version}-%{release}

%description
No detailed description available

%package data
Summary: data components for the mvn-maven-toolchain package.
Group: Data

%description data
data components for the mvn-maven-toolchain package.


%package license
Summary: license components for the mvn-maven-toolchain package.
Group: Default

%description license
license components for the mvn-maven-toolchain package.


%prep
%setup -q -n META-INF

%build

%install
mkdir -p %{buildroot}/usr/share/package-licenses/mvn-maven-toolchain
cp LICENSE %{buildroot}/usr/share/package-licenses/mvn-maven-toolchain/LICENSE
cp NOTICE %{buildroot}/usr/share/package-licenses/mvn-maven-toolchain/NOTICE
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-toolchain/2.2.1
cp %{SOURCE0} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-toolchain/2.2.1/maven-toolchain-2.2.1.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-toolchain/1.0
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-toolchain/1.0/maven-toolchain-1.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-toolchain/1.0
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-toolchain/1.0/maven-toolchain-1.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-toolchain/2.0.9
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-toolchain/2.0.9/maven-toolchain-2.0.9.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-toolchain/2.0.9
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-toolchain/2.0.9/maven-toolchain-2.0.9.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-toolchain/2.1.0
cp %{SOURCE5} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-toolchain/2.1.0/maven-toolchain-2.1.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-toolchain/2.1.0
cp %{SOURCE6} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-toolchain/2.1.0/maven-toolchain-2.1.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-toolchain/2.2.1
cp %{SOURCE7} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-toolchain/2.2.1/maven-toolchain-2.2.1.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/apache/maven/maven-toolchain/1.0/maven-toolchain-1.0.jar
/usr/share/java/.m2/repository/org/apache/maven/maven-toolchain/1.0/maven-toolchain-1.0.pom
/usr/share/java/.m2/repository/org/apache/maven/maven-toolchain/2.0.9/maven-toolchain-2.0.9.jar
/usr/share/java/.m2/repository/org/apache/maven/maven-toolchain/2.0.9/maven-toolchain-2.0.9.pom
/usr/share/java/.m2/repository/org/apache/maven/maven-toolchain/2.1.0/maven-toolchain-2.1.0.jar
/usr/share/java/.m2/repository/org/apache/maven/maven-toolchain/2.1.0/maven-toolchain-2.1.0.pom
/usr/share/java/.m2/repository/org/apache/maven/maven-toolchain/2.2.1/maven-toolchain-2.2.1.jar
/usr/share/java/.m2/repository/org/apache/maven/maven-toolchain/2.2.1/maven-toolchain-2.2.1.pom

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mvn-maven-toolchain/LICENSE
/usr/share/package-licenses/mvn-maven-toolchain/NOTICE
