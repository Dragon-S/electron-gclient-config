solutions = [
  { "name"        : "src/electron",
    "url"         : "https://github.com/Dragon-S/electron.git@ddd8c4227de8d8cc97ea28090495978a1d466736",
    "deps_file"   : "DEPS",
    "managed"     : False,
    "custom_deps" : {
      "src/third_party/webrtc": "https://github.com/Dragon-S/google-webrtc.git@bac9ef7e7f13abbf874f5c32881165bba27af020",
      "src/third_party/openh264/src": "https://chromium.googlesource.com/external/github.com/cisco/openh264@09a4f3ec842a8932341b195c5b01e141c8a16eb7",
    },
    "custom_vars": {},
  },
]