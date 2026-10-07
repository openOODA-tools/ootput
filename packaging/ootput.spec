Name:           ootput
Version:        0.1.0
Release:        1%{?dist}
Summary:        Zero-dependency terminfo querying for terminal capabilities, colors, and cursor movements.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/ootput
Source0:        ootput-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
ootput is a sovereign, capability-bounded TERMINFO QUERY written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/ootput
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/ootput-uninstall

%files
/usr/bin/ootput
/usr/bin/ootput-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
