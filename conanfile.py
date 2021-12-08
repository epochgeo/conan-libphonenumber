
import os

from conans import ConanFile, tools, CMake
from conan.tools.layout import cmake_layout


class LibphonenumberConan(ConanFile):
    name = "libphonenumber"
    version = "8.12.27"

    # Optional metadata
    license = "Apache v2 License"
    homepage = "https://github.com/google/libphonenumber"
    url = "https://github.com/conan-io/conan-center-index"
    description = "Google's common Java, C++ and JavaScript library for parsing, formatting, and validating international phone numbers."
    exports_sources = ["CMakeLists.txt"]
    generators = "cmake", "cmake_find_package"

    # Binary configuration
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}

    requires = [
        "boost/[>=1.71]",
        "protobuf/[>=3.15]",
    ]

    @property
    def _build_subfolder(self):
        return "build_subfolder"

    @property
    def _source_subfolder(self):
        return "source_subfolder"

    def source(self):
        url = f"https://github.com/google/libphonenumber/archive/refs/tags/v{self.version}.tar.gz"
        tools.get(url=url, strip_root=True, destination=self._source_subfolder)

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def build(self):
        cmake = CMake(self)
        cmake.configure(build_folder=self._build_subfolder)
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.configure(build_folder=self._build_subfolder)
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["phonenumber"]