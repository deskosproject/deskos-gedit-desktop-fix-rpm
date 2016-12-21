Name:           deskos-gedit-desktop-fix
Version:        1.0
Release:        1%{?dist}
Summary:        DeskOS fix for duplicate gedit desktop file

Group:          Applications/Editors
License:        GPLv3
URL:            https://deskosproject.org

Requires:       gedit

%description
DeskOS fix for GNOME 3.14 showing two gedit entries for the "Open With" menu.
It removes the /usr/share/applications/gedit.desktop file, part of the gedit EL7 package.

Related to this bug:
https://bugzilla.redhat.com/show_bug.cgi?id=1238207

This package is necessary since gedit could not be patched and rebuilt for DeskOS 7.3:
https://bugzilla.redhat.com/show_bug.cgi?id=1387681

%files

%post
rm -f /usr/share/applications/gedit.desktop
/usr/bin/update-desktop-database

%changelog
* Wed Dec 21 2016 Ricardo Arguello <rarguello@deskosproject.org> - 1.0-1
- Initial DeskOS release
