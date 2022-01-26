# -*- coding: utf8 -*-
# Copyright (c) 2019 Niklas Rosenstein
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

import typing as t

import docspec
import os


class HighlightResolver:
    def __init__(self, modules: t.List[docspec.Module]) -> None:
        self.modules = modules
        self.dummyClass = docspec.Class(
            "dummy_class", None, None, None, None, None, None, None, None
        )

    def GetObjectID(self, obj: docspec.ApiObject) -> str:
        parts = []
        while obj:
            parts.append(obj.name)
            obj = obj.parent
        return ".".join(reversed(parts))

    def GetObjectModule(self, obj: docspec.ApiObject) -> docspec.Module:
        while type(obj) != docspec.Module:
            obj = obj.parent
        return obj

    def FindModuleByName(self, moduleName: str) -> t.Optional[docspec.Module]:
        for module in self.modules:
            if module.name == moduleName:
                return module
        return None

    def FindRefInModule(
        self,
        module: docspec.Module,
        refNames: t.List[str],
        typeFilter: t.List[t.Type[docspec.ApiObject]] = [],
    ) -> t.Optional[docspec.ApiObject]:

        if isinstance(refNames, str):
            refNames = [refNames]

        def find(module: docspec.Module, name: str) -> t.Optional[docspec.ApiObject]:

            for member in module.members:
                if (
                    member.name == partName
                    and ((len(typeFilter) == 0) or (type(member) in typeFilter))
                    # and not isinstance(member, docspec.Indirection)
                ):
                    return member

            return None

        checkObj = module
        for partName in refNames:
            if not isinstance(checkObj, docspec.HasMembers):
                return None

            # checkObj = next((member for member in checkObj.members if member.name == partName and not isinstance(member, docspec.Indirection)), None)
            checkObj = find(checkObj, partName)
            if checkObj == None:
                break

        return checkObj

    def FindAllReference(
        self,
        obj: docspec.ApiObject,
        refNames: t.List[str],
        typeFilter: t.List[t.Type[docspec.ApiObject]] = [],
        excpt: docspec.ApiObject = None,
        inherited: bool = False,
    ) -> t.Tuple[t.List[docspec.ApiObject], t.List[docspec.ApiObject]]:
        """
        Find all the references in all files
        """

        easyFind = self.FindRefInModule(obj, refNames[-1], typeFilter)
        hardFind = self.FindRefInModule(obj, refNames, typeFilter)
        easyResults = [easyFind] if easyFind != None else []
        hardResults = [hardFind] if hardFind != None else []

        if isinstance(obj, docspec.HasMembers):
            for member in obj.members:
                if member != excpt:
                    search = self.FindAllReference(
                        member, refNames, typeFilter, None, True
                    )
                    easyResults.extend(search[0])
                    hardResults.extend(search[1])

        if not inherited:

            parent = obj.parent

            if parent == None:
                for module in self.modules:
                    if module != excpt:
                        search = self.FindAllReference(
                            module, refNames, typeFilter, None, True
                        )
                        easyResults.extend(search[0])
                        hardResults.extend(search[1])
            else:
                search = self.FindAllReference(parent, refNames, typeFilter, obj, False)
                easyResults.extend(search[0])
                hardResults.extend(search[1])

        return (easyResults, hardResults)

    def resolve_ref(
        self,
        reference: str,
        typeFilter: t.List[t.Type[docspec.ApiObject]] = [],
    ) -> t.Optional[docspec.ApiObject]:

        obj = self.modules[0]
        while True:
            parent = obj.parent
            if parent == None:
                break
            obj = parent

        refNames = reference.split(".")
        easyResult, hardResult = self.FindAllReference(obj, refNames, typeFilter)

        for result in hardResult:
            return result

        for result in easyResult:
            return result

        return None
