solutions = [
  { "name"        : "src/electron",
    "url"         : "https://github.com/Dragon-S/electron.git@7c4184aabb3494139a17c218bb97f2e9374ed128",
    "deps_file"   : "DEPS",
    "managed"     : False,
    "custom_deps" : {
      "src/third_party/webrtc": "https://github.com/Dragon-S/google-webrtc.git@0e70ea50a8a7da6db343334006afc884e13839f0",
      "src/third_party/openh264/src": "https://chromium.googlesource.com/external/github.com/cisco/openh264@09a4f3ec842a8932341b195c5b01e141c8a16eb7",
    },
    "custom_vars": {},
  },
]