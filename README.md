# Unofficial_KeyShot_Python
Unofficial KeyShot Python Libraries and Documentation 
# KeyShot Python API Documentation

Welcome to the KeyShot Python API Documentation repository. This resource is created to provide comprehensive guides, detailed documentation, and practical script examples for users of KeyShot's Python API. Whether you're automating tasks in KeyShot, extending its functionalities, or integrating KeyShot into your digital pipeline, this repository aims to be your go-to reference.

## What is this?

An unofficial reference for KeyShot's Python interfaces, with example scripts
for scene access, transforms, cameras, materials, import, and rendering.

## Why care?

Suppose a product scene contains many parts and you need to inspect or adjust
them consistently. A script can turn that repeated scene work into an explicit
sequence you can review and reuse. This repository provides examples and API
notes to help build that sequence.

## Try this

Open [Accessing Scene Nodes](Scripts/Accessing%20Scene%20Nodes.txt) and compare
the example with your scene tree. Then read
[Transforming scene nodes](Scripts/Scripting%20Transforming%20scene%20nodes.txt)
to see how selection and transforms connect. Try edits on a copy of a scene in
a KeyShot installation with scripting support; the examples use KeyShot's
environment, not standalone Python.


## Table of Contents

- [Introduction](#introduction)
- [lux Library Documentation](#lux-library-documentation)
- [luxmath Library Documentation](#luxmath-library-documentation)
- [Headless Mode Documentation](#headless-mode-documentation)
  - [lux Headless](#lux-headless)
  - [luxmath Headless](#luxmath-headless)
- [Example Scripts](#example-scripts)
- [Contributing](#contributing)
- [License](#license)

## Introduction

KeyShot by Luxion is a leading real-time 3D rendering and animation software. The KeyShot Python API allows for scripting and automation of various KeyShot functionalities, enhancing productivity and enabling advanced customizations. This repository documents the `lux` and `luxmath` libraries, provides insights into running KeyShot in headless mode, and shares useful script examples.

## lux Library Documentation

The `lux` library is KeyShot's primary interface for scripting, offering functions to control scenes, materials, cameras, rendering, and more. [Explore the lux library documentation.](lux/KeyShot_lux_API.md)

## luxmath Library Documentation

For mathematical operations, the `luxmath` library provides Vector and Matrix classes, essential for transformations and other calculations in scripts. [Learn more about luxmath.](luxmath/KeyShot_luxmath_API.md)

## Headless Mode Documentation

Running KeyShot in headless mode enables automation and integration into pipelines without the GUI. This section covers the essentials for both `lux` and `luxmath` libraries in headless operation.

### lux Headless

Documentation specific to using the `lux` library without the KeyShot interface. [Dive into lux headless mode.](lux_headless/KeyShot_headless_lux_API.md)

### luxmath Headless

Similar to the `luxmath` library, but focused on headless applications. [Discover luxmath in headless mode.](luxmath_headless/KeyShot_headless_luxmath_API.md)

## Example Scripts

A collection of scripts demonstrating the practical application of KeyShot's Python API for common tasks and advanced customizations. [Browse example scripts.](Scripts/)

## Contributing

Contributions to this repository are welcome! Whether it's improving documentation, adding new scripts, or reporting issues, your input helps make this resource better for everyone. [Find out how to contribute.](CONTRIBUTING.md)

## License

This project is licensed under [MIT License](LICENSE) - see the LICENSE file for details.
