solutions = [
  { "name"        : "src/electron",
    "url"         : "https://github.com/Dragon-S/electron.git@18fc04471b467320019671dbf250dc46e1679296",
    "deps_file"   : "DEPS",
    "managed"     : False,
    "custom_deps" : {
      "src/third_party/webrtc": "https://github.com/Dragon-S/google-webrtc.git@150ad5188f16aca1f32758fa28afabc498f955c5",
    },
    "custom_vars": {},
  },
]