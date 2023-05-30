solutions = [
  { "name"        : "src/electron",
    "url"         : "https://github.com/Dragon-S/electron.git@611b1b2d9c898d5e8c58c7635ab3fb9a31dcf588",
    "deps_file"   : "DEPS",
    "managed"     : False,
    "custom_deps" : {
      "src/third_party/webrtc": "https://github.com/Dragon-S/google-webrtc.git@0e70ea50a8a7da6db343334006afc884e13839f0",
      "src/third_party/openh264/src": "https://chromium.googlesource.com/external/github.com/cisco/openh264@09a4f3ec842a8932341b195c5b01e141c8a16eb7",
    },
    "custom_vars": {},
  },
]