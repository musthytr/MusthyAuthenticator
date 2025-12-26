[Setup]
AppName=MusthyAuthenticator
AppVersion=1.0
DefaultDirName={sd}\MAUTH
DefaultGroupName=MusthyAuthenticator
OutputDir=installer
OutputBaseFilename=MusthyAuthenticatorSetup
Compression=lzma
SolidCompression=yes
PrivilegesRequired=lowest

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "Create a desktop shortcut"; GroupDescription: "Additional icons:"

[Files]
Source: "dist\MusthyAuthenticator.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{commondesktop}\MusthyAuthenticator"; Filename: "{app}\MusthyAuthenticator.exe"; Tasks: desktopicon

[Run]
Filename: "{app}\MusthyAuthenticator.exe"; Description: "Launch MusthyAuthenticator"; Flags: nowait postinstall skipifsilent