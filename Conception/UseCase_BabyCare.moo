<?xml version="1.0" encoding="UTF-8"?>
<?PowerDesigner AppLocale="UTF16" ID="{BFF891C5-515C-4407-83E4-5AFE470F7B56}" Label="" LastModificationDate="1767559223" Name="UseCase_BabyCare" Objects="68" Symbols="84" Target="Java" TargetLink="Reference" Type="{18112060-1A4B-11D1-83D9-444553540000}" signature="CLD_OBJECT_MODEL" version="15.1.0.2850"?>
<!-- Veuillez ne pas modifier ce fichier -->

<Model xmlns:a="attribute" xmlns:c="collection" xmlns:o="object">

<o:RootObject Id="o1">
<c:Children>
<o:Model Id="o2">
<a:ObjectID>BFF891C5-515C-4407-83E4-5AFE470F7B56</a:ObjectID>
<a:Name>UseCase_BabyCare</a:Name>
<a:Code>UseCase_BabyCare</a:Code>
<a:CreationDate>1767020302</a:CreationDate>
<a:Creator>houda</a:Creator>
<a:ModificationDate>1767559042</a:ModificationDate>
<a:Modifier>houda</a:Modifier>
<a:PackageOptionsText>[FolderOptions]

[FolderOptions\Class Diagram Objects]
GenerationCheckModel=Yes
GenerationPath=
GenerationOptions=
GenerationTasks=
GenerationTargets=
GenerationSelections=</a:PackageOptionsText>
<a:ModelOptionsText>[ModelOptions]

[ModelOptions\Cld]
CaseSensitive=Yes
DisplayName=Yes
EnableTrans=Yes
EnableRequirements=No
ShowClss=No
DeftAttr=int
DeftMthd=int
DeftParm=int
DeftCont=java.util.Collection
DomnDttp=Yes
DomnChck=No
DomnRule=No
SupportDelay=No
PreviewEditable=Yes
AutoRealize=No
DttpFullName=Yes
DeftClssAttrVisi=private
VBNetPreprocessingSymbols=
CSharpPreprocessingSymbols=

[ModelOptions\Cld\NamingOptionsTemplates]

[ModelOptions\Cld\ClssNamingOptions]

[ModelOptions\Cld\ClssNamingOptions\CLDPCKG]

[ModelOptions\Cld\ClssNamingOptions\CLDPCKG\Name]
Template=
MaxLen=254
Case=M
ValidChar=
InvldChar=
AllValid=Yes
NoAccent=No
DefaultChar=_
Script=.convert_name(%Name%,,,firstLowerWord)
ConvTable=
ConvTablePath=%_HOME%\Fichiers de ressources\Tables de conversion

[ModelOptions\Cld\ClssNamingOptions\CLDPCKG\Code]
Template=
MaxLen=254
Case=M
ValidChar=&#39;a&#39;-&#39;z&#39;,&#39;A&#39;-&#39;Z&#39;,&#39;0&#39;-&#39;9&#39;,&quot;_&quot;
InvldChar=&quot; &#39;(.)+=*/&quot;
AllValid=Yes
NoAccent=Yes
DefaultChar=_
Script=.convert_code(%Code%,&quot; &quot;)
ConvTable=
ConvTablePath=%_HOME%\Fichiers de ressources\Tables de conversion

[ModelOptions\Cld\ClssNamingOptions\CLDDOMN]

[ModelOptions\Cld\ClssNamingOptions\CLDDOMN\Name]
Template=
MaxLen=254
Case=M
ValidChar=
InvldChar=
AllValid=Yes
NoAccent=No
DefaultChar=_
Script=.convert_name(%Name%,&quot;_&quot;)
ConvTable=
ConvTablePath=%_HOME%\Fichiers de ressources\Tables de conversion

[ModelOptions\Cld\ClssNamingOptions\CLDDOMN\Code]
Template=
MaxLen=254
Case=M
ValidChar=&#39;a&#39;-&#39;z&#39;,&#39;A&#39;-&#39;Z&#39;,&#39;0&#39;-&#39;9&#39;,&quot;_&quot;
InvldChar=&quot; &#39;(.)+=*/&quot;
AllValid=Yes
NoAccent=Yes
DefaultChar=_
Script=.convert_code(%Code%,&quot; &quot;)
ConvTable=
ConvTablePath=%_HOME%\Fichiers de ressources\Tables de conversion

[ModelOptions\Cld\ClssNamingOptions\CLDCLASS]

[ModelOptions\Cld\ClssNamingOptions\CLDCLASS\Name]
Template=
MaxLen=254
Case=M
ValidChar=
InvldChar=
AllValid=Yes
NoAccent=No
DefaultChar=_
Script=.convert_name(%Name%,,,FirstUpperChar)
ConvTable=
ConvTablePath=%_HOME%\Fichiers de ressources\Tables de conversion

[ModelOptions\Cld\ClssNamingOptions\CLDCLASS\Code]
Template=
MaxLen=254
Case=M
ValidChar=&#39;a&#39;-&#39;z&#39;,&#39;A&#39;-&#39;Z&#39;,&#39;0&#39;-&#39;9&#39;,&quot;_&quot;
InvldChar=&quot; &#39;(.)+=*/&quot;
AllValid=Yes
NoAccent=Yes
DefaultChar=_
Script=.convert_code(%Code%,&quot; &quot;)
ConvTable=
ConvTablePath=%_HOME%\Fichiers de ressources\Tables de conversion

[ModelOptions\Cld\ClssNamingOptions\CLDINTF]

[ModelOptions\Cld\ClssNamingOptions\CLDINTF\Name]
Template=
MaxLen=254
Case=M
ValidChar=
InvldChar=
AllValid=Yes
NoAccent=No
DefaultChar=_
Script=.convert_name(%Name%,,,FirstUpperChar)
ConvTable=
ConvTablePath=%_HOME%\Fichiers de ressources\Tables de conversion

[ModelOptions\Cld\ClssNamingOptions\CLDINTF\Code]
Template=
MaxLen=254
Case=M
ValidChar=&#39;a&#39;-&#39;z&#39;,&#39;A&#39;-&#39;Z&#39;,&#39;0&#39;-&#39;9&#39;,&quot;_&quot;
InvldChar=&quot; &#39;(.)+=*/&quot;
AllValid=Yes
NoAccent=Yes
DefaultChar=_
Script=.convert_code(%Code%,&quot; &quot;)
ConvTable=
ConvTablePath=%_HOME%\Fichiers de ressources\Tables de conversion

[ModelOptions\Cld\ClssNamingOptions\UCDACTR]

[ModelOptions\Cld\ClssNamingOptions\UCDACTR\Name]
Template=
MaxLen=254
Case=M
ValidChar=
InvldChar=
AllValid=Yes
NoAccent=No
DefaultChar=_
Script=.convert_name(%Name%,&quot;_&quot;)
ConvTable=
ConvTablePath=%_HOME%\Fichiers de ressources\Tables de conversion

[ModelOptions\Cld\ClssNamingOptions\UCDACTR\Code]
Template=
MaxLen=254
Case=M
ValidChar=&#39;a&#39;-&#39;z&#39;,&#39;A&#39;-&#39;Z&#39;,&#39;0&#39;-&#39;9&#39;,&quot;_&quot;
InvldChar=&quot; &#39;(.)+=*/&quot;
AllValid=Yes
NoAccent=Yes
DefaultChar=_
Script=.convert_code(%Code%,&quot; &quot;)
ConvTable=
ConvTablePath=%_HOME%\Fichiers de ressources\Tables de conversion

[ModelOptions\Cld\ClssNamingOptions\UCDUCAS]

[ModelOptions\Cld\ClssNamingOptions\UCDUCAS\Name]
Template=
MaxLen=254
Case=M
ValidChar=
InvldChar=
AllValid=Yes
NoAccent=No
DefaultChar=_
Script=.convert_name(%Name%,&quot;_&quot;)
ConvTable=
ConvTablePath=%_HOME%\Fichiers de ressources\Tables de conversion

[ModelOptions\Cld\ClssNamingOptions\UCDUCAS\Code]
Template=
MaxLen=254
Case=M
ValidChar=&#39;a&#39;-&#39;z&#39;,&#39;A&#39;-&#39;Z&#39;,&#39;0&#39;-&#39;9&#39;,&quot;_&quot;
InvldChar=&quot; &#39;(.)+=*/&quot;
AllValid=Yes
NoAccent=Yes
DefaultChar=_
Script=.convert_code(%Code%,&quot; &quot;)
ConvTable=
ConvTablePath=%_HOME%\Fichiers de ressources\Tables de conversion

[ModelOptions\Cld\ClssNamingOptions\SQDOBJT]

[ModelOptions\Cld\ClssNamingOptions\SQDOBJT\Name]
Template=
MaxLen=254
Case=M
ValidChar=
InvldChar=
AllValid=Yes
NoAccent=No
DefaultChar=_
Script=.convert_name(%Name%,&quot;_&quot;)
ConvTable=
ConvTablePath=%_HOME%\Fichiers de ressources\Tables de conversion

[ModelOptions\Cld\ClssNamingOptions\SQDOBJT\Code]
Template=
MaxLen=254
Case=M
ValidChar=&#39;a&#39;-&#39;z&#39;,&#39;A&#39;-&#39;Z&#39;,&#39;0&#39;-&#39;9&#39;,&quot;_&quot;
InvldChar=&quot; &#39;(.)+=*/&quot;
AllValid=Yes
NoAccent=Yes
DefaultChar=_
Script=.convert_code(%Code%,&quot; &quot;)
ConvTable=
ConvTablePath=%_HOME%\Fichiers de ressources\Tables de conversion

[ModelOptions\Cld\ClssNamingOptions\SQDMSSG]

[ModelOptions\Cld\ClssNamingOptions\SQDMSSG\Name]
Template=
MaxLen=254
Case=M
ValidChar=
InvldChar=
AllValid=Yes
NoAccent=No
DefaultChar=_
Script=.convert_name(%Name%,&quot;_&quot;)
ConvTable=
ConvTablePath=%_HOME%\Fichiers de ressources\Tables de conversion

[ModelOptions\Cld\ClssNamingOptions\SQDMSSG\Code]
Template=
MaxLen=254
Case=M
ValidChar=&#39;a&#39;-&#39;z&#39;,&#39;A&#39;-&#39;Z&#39;,&#39;0&#39;-&#39;9&#39;,&quot;_&quot;
InvldChar=&quot; &#39;(.)+=*/&quot;
AllValid=Yes
NoAccent=Yes
DefaultChar=_
Script=.convert_code(%Code%,&quot; &quot;)
ConvTable=
ConvTablePath=%_HOME%\Fichiers de ressources\Tables de conversion

[ModelOptions\Cld\ClssNamingOptions\CPDCOMP]

[ModelOptions\Cld\ClssNamingOptions\CPDCOMP\Name]
Template=
MaxLen=254
Case=M
ValidChar=
InvldChar=
AllValid=Yes
NoAccent=No
DefaultChar=_
Script=.convert_name(%Name%,,,FirstUpperChar)
ConvTable=
ConvTablePath=%_HOME%\Fichiers de ressources\Tables de conversion

[ModelOptions\Cld\ClssNamingOptions\CPDCOMP\Code]
Template=
MaxLen=254
Case=M
ValidChar=&#39;a&#39;-&#39;z&#39;,&#39;A&#39;-&#39;Z&#39;,&#39;0&#39;-&#39;9&#39;,&quot;_&quot;
InvldChar=&quot; &#39;(.)+=*/&quot;
AllValid=Yes
NoAccent=Yes
DefaultChar=_
Script=.convert_code(%Code%,&quot; &quot;)
ConvTable=
ConvTablePath=%_HOME%\Fichiers de ressources\Tables de conversion

[ModelOptions\Cld\ClssNamingOptions\CLDATTR]

[ModelOptions\Cld\ClssNamingOptions\CLDATTR\Name]
Template=
MaxLen=254
Case=M
ValidChar=
InvldChar=
AllValid=Yes
NoAccent=No
DefaultChar=_
Script=.convert_name(%Name%,,,firstLowerWord)
ConvTable=
ConvTablePath=%_HOME%\Fichiers de ressources\Tables de conversion

[ModelOptions\Cld\ClssNamingOptions\CLDATTR\Code]
Template=
MaxLen=254
Case=M
ValidChar=&#39;a&#39;-&#39;z&#39;,&#39;A&#39;-&#39;Z&#39;,&#39;0&#39;-&#39;9&#39;,&quot;_&quot;
InvldChar=&quot; &#39;(.)+=*/&quot;
AllValid=Yes
NoAccent=Yes
DefaultChar=_
Script=.convert_code(%Code%,&quot; &quot;)
ConvTable=
ConvTablePath=%_HOME%\Fichiers de ressources\Tables de conversion

[ModelOptions\Cld\ClssNamingOptions\CLDMETHOD]

[ModelOptions\Cld\ClssNamingOptions\CLDMETHOD\Name]
Template=
MaxLen=254
Case=M
ValidChar=
InvldChar=
AllValid=Yes
NoAccent=No
DefaultChar=_
Script=.convert_name(%Name%,,,firstLowerWord)
ConvTable=
ConvTablePath=%_HOME%\Fichiers de ressources\Tables de conversion

[ModelOptions\Cld\ClssNamingOptions\CLDMETHOD\Code]
Template=
MaxLen=254
Case=M
ValidChar=&#39;a&#39;-&#39;z&#39;,&#39;A&#39;-&#39;Z&#39;,&#39;0&#39;-&#39;9&#39;,&quot;_&quot;
InvldChar=&quot; &#39;(.)+=*/&quot;
AllValid=Yes
NoAccent=Yes
DefaultChar=_
Script=.convert_code(%Code%,&quot; &quot;)
ConvTable=
ConvTablePath=%_HOME%\Fichiers de ressources\Tables de conversion

[ModelOptions\Cld\ClssNamingOptions\CLDPARM]

[ModelOptions\Cld\ClssNamingOptions\CLDPARM\Name]
Template=
MaxLen=254
Case=M
ValidChar=
InvldChar=
AllValid=Yes
NoAccent=No
DefaultChar=_
Script=.convert_name(%Name%,,,firstLowerWord)
ConvTable=
ConvTablePath=%_HOME%\Fichiers de ressources\Tables de conversion

[ModelOptions\Cld\ClssNamingOptions\CLDPARM\Code]
Template=
MaxLen=254
Case=M
ValidChar=&#39;a&#39;-&#39;z&#39;,&#39;A&#39;-&#39;Z&#39;,&#39;0&#39;-&#39;9&#39;,&quot;_&quot;
InvldChar=&quot; &#39;(.)+=*/&quot;
AllValid=Yes
NoAccent=Yes
DefaultChar=_
Script=.convert_code(%Code%,&quot; &quot;)
ConvTable=
ConvTablePath=%_HOME%\Fichiers de ressources\Tables de conversion

[ModelOptions\Cld\ClssNamingOptions\OOMPORT]

[ModelOptions\Cld\ClssNamingOptions\OOMPORT\Name]
Template=
MaxLen=254
Case=M
ValidChar=
InvldChar=
AllValid=Yes
NoAccent=No
DefaultChar=_
Script=.convert_name(%Name%,&quot;_&quot;)
ConvTable=
ConvTablePath=%_HOME%\Fichiers de ressources\Tables de conversion

[ModelOptions\Cld\ClssNamingOptions\OOMPORT\Code]
Template=
MaxLen=254
Case=M
ValidChar=&#39;a&#39;-&#39;z&#39;,&#39;A&#39;-&#39;Z&#39;,&#39;0&#39;-&#39;9&#39;,&quot;_&quot;
InvldChar=&quot; &#39;(.)+=*/&quot;
AllValid=Yes
NoAccent=Yes
DefaultChar=_
Script=.convert_code(%Code%,&quot; &quot;)
ConvTable=
ConvTablePath=%_HOME%\Fichiers de ressources\Tables de conversion

[ModelOptions\Cld\ClssNamingOptions\OOMPART]

[ModelOptions\Cld\ClssNamingOptions\OOMPART\Name]
Template=
MaxLen=254
Case=M
ValidChar=
InvldChar=
AllValid=Yes
NoAccent=No
DefaultChar=_
Script=.convert_name(%Name%,&quot;_&quot;)
ConvTable=
ConvTablePath=%_HOME%\Fichiers de ressources\Tables de conversion

[ModelOptions\Cld\ClssNamingOptions\OOMPART\Code]
Template=
MaxLen=254
Case=M
ValidChar=&#39;a&#39;-&#39;z&#39;,&#39;A&#39;-&#39;Z&#39;,&#39;0&#39;-&#39;9&#39;,&quot;_&quot;
InvldChar=&quot; &#39;(.)+=*/&quot;
AllValid=Yes
NoAccent=Yes
DefaultChar=_
Script=.convert_code(%Code%,&quot; &quot;)
ConvTable=
ConvTablePath=%_HOME%\Fichiers de ressources\Tables de conversion

[ModelOptions\Cld\ClssNamingOptions\CLDASSC]

[ModelOptions\Cld\ClssNamingOptions\CLDASSC\Name]
Template=
MaxLen=254
Case=M
ValidChar=
InvldChar=
AllValid=Yes
NoAccent=No
DefaultChar=_
Script=.convert_name(%Name%,,,firstLowerWord)
ConvTable=
ConvTablePath=%_HOME%\Fichiers de ressources\Tables de conversion

[ModelOptions\Cld\ClssNamingOptions\CLDASSC\Code]
Template=
MaxLen=254
Case=M
ValidChar=&#39;a&#39;-&#39;z&#39;,&#39;A&#39;-&#39;Z&#39;,&#39;0&#39;-&#39;9&#39;,&quot;_&quot;
InvldChar=&quot; &#39;(.)+=*/&quot;
AllValid=Yes
NoAccent=Yes
DefaultChar=_
Script=.convert_code(%Code%,&quot; &quot;)
ConvTable=
ConvTablePath=%_HOME%\Fichiers de ressources\Tables de conversion

[ModelOptions\Cld\ClssNamingOptions\UCDASSC]

[ModelOptions\Cld\ClssNamingOptions\UCDASSC\Name]
Template=
MaxLen=254
Case=M
ValidChar=
InvldChar=
AllValid=Yes
NoAccent=No
DefaultChar=_
Script=.convert_name(%Name%,&quot;_&quot;)
ConvTable=
ConvTablePath=%_HOME%\Fichiers de ressources\Tables de conversion

[ModelOptions\Cld\ClssNamingOptions\UCDASSC\Code]
Template=
MaxLen=254
Case=M
ValidChar=&#39;a&#39;-&#39;z&#39;,&#39;A&#39;-&#39;Z&#39;,&#39;0&#39;-&#39;9&#39;,&quot;_&quot;
InvldChar=&quot; &#39;(.)+=*/&quot;
AllValid=Yes
NoAccent=Yes
DefaultChar=_
Script=.convert_code(%Code%,&quot; &quot;)
ConvTable=
ConvTablePath=%_HOME%\Fichiers de ressources\Tables de conversion

[ModelOptions\Cld\ClssNamingOptions\GNRLLINK]

[ModelOptions\Cld\ClssNamingOptions\GNRLLINK\Name]
Template=
MaxLen=254
Case=M
ValidChar=
InvldChar=
AllValid=Yes
NoAccent=No
DefaultChar=_
Script=.convert_name(%Name%,&quot;_&quot;)
ConvTable=
ConvTablePath=%_HOME%\Fichiers de ressources\Tables de conversion

[ModelOptions\Cld\ClssNamingOptions\GNRLLINK\Code]
Template=
MaxLen=254
Case=M
ValidChar=&#39;a&#39;-&#39;z&#39;,&#39;A&#39;-&#39;Z&#39;,&#39;0&#39;-&#39;9&#39;,&quot;_&quot;
InvldChar=&quot; &#39;(.)+=*/&quot;
AllValid=Yes
NoAccent=Yes
DefaultChar=_
Script=.convert_code(%Code%,&quot; &quot;)
ConvTable=
ConvTablePath=%_HOME%\Fichiers de ressources\Tables de conversion

[ModelOptions\Cld\ClssNamingOptions\RQLINK]

[ModelOptions\Cld\ClssNamingOptions\RQLINK\Name]
Template=
MaxLen=254
Case=M
ValidChar=
InvldChar=
AllValid=Yes
NoAccent=No
DefaultChar=_
Script=.convert_name(%Name%,&quot;_&quot;)
ConvTable=
ConvTablePath=%_HOME%\Fichiers de ressources\Tables de conversion

[ModelOptions\Cld\ClssNamingOptions\RQLINK\Code]
Template=
MaxLen=254
Case=M
ValidChar=&#39;a&#39;-&#39;z&#39;,&#39;A&#39;-&#39;Z&#39;,&#39;0&#39;-&#39;9&#39;,&quot;_&quot;
InvldChar=&quot; &#39;(.)+=*/&quot;
AllValid=Yes
NoAccent=Yes
DefaultChar=_
Script=.convert_code(%Code%,&quot; &quot;)
ConvTable=
ConvTablePath=%_HOME%\Fichiers de ressources\Tables de conversion

[ModelOptions\Cld\ClssNamingOptions\RLZSLINK]

[ModelOptions\Cld\ClssNamingOptions\RLZSLINK\Name]
Template=
MaxLen=254
Case=M
ValidChar=
InvldChar=
AllValid=Yes
NoAccent=No
DefaultChar=_
Script=.convert_name(%Name%,&quot;_&quot;)
ConvTable=
ConvTablePath=%_HOME%\Fichiers de ressources\Tables de conversion

[ModelOptions\Cld\ClssNamingOptions\RLZSLINK\Code]
Template=
MaxLen=254
Case=M
ValidChar=&#39;a&#39;-&#39;z&#39;,&#39;A&#39;-&#39;Z&#39;,&#39;0&#39;-&#39;9&#39;,&quot;_&quot;
InvldChar=&quot; &#39;(.)+=*/&quot;
AllValid=Yes
NoAccent=Yes
DefaultChar=_
Script=.convert_code(%Code%,&quot; &quot;)
ConvTable=
ConvTablePath=%_HOME%\Fichiers de ressources\Tables de conversion

[ModelOptions\Cld\ClssNamingOptions\DEPDLINK]

[ModelOptions\Cld\ClssNamingOptions\DEPDLINK\Name]
Template=
MaxLen=254
Case=M
ValidChar=
InvldChar=
AllValid=Yes
NoAccent=No
DefaultChar=_
Script=.convert_name(%Name%,&quot;_&quot;)
ConvTable=
ConvTablePath=%_HOME%\Fichiers de ressources\Tables de conversion

[ModelOptions\Cld\ClssNamingOptions\DEPDLINK\Code]
Template=
MaxLen=254
Case=M
ValidChar=&#39;a&#39;-&#39;z&#39;,&#39;A&#39;-&#39;Z&#39;,&#39;0&#39;-&#39;9&#39;,&quot;_&quot;
InvldChar=&quot; &#39;(.)+=*/&quot;
AllValid=Yes
NoAccent=Yes
DefaultChar=_
Script=.convert_code(%Code%,&quot; &quot;)
ConvTable=
ConvTablePath=%_HOME%\Fichiers de ressources\Tables de conversion

[ModelOptions\Cld\ClssNamingOptions\OOMACTV]

[ModelOptions\Cld\ClssNamingOptions\OOMACTV\Name]
Template=
MaxLen=254
Case=M
ValidChar=
InvldChar=
AllValid=Yes
NoAccent=No
DefaultChar=_
Script=.convert_name(%Name%,&quot;_&quot;)
ConvTable=
ConvTablePath=%_HOME%\Fichiers de ressources\Tables de conversion

[ModelOptions\Cld\ClssNamingOptions\OOMACTV\Code]
Template=
MaxLen=254
Case=M
ValidChar=&#39;a&#39;-&#39;z&#39;,&#39;A&#39;-&#39;Z&#39;,&#39;0&#39;-&#39;9&#39;,&quot;_&quot;
InvldChar=&quot; &#39;(.)+=*/&quot;
AllValid=Yes
NoAccent=Yes
DefaultChar=_
Script=.convert_code(%Code%,&quot; &quot;)
ConvTable=
ConvTablePath=%_HOME%\Fichiers de ressources\Tables de conversion

[ModelOptions\Cld\ClssNamingOptions\ACDOBST]

[ModelOptions\Cld\ClssNamingOptions\ACDOBST\Name]
Template=
MaxLen=254
Case=M
ValidChar=
InvldChar=
AllValid=Yes
NoAccent=No
DefaultChar=_
Script=.convert_name(%Name%,&quot;_&quot;)
ConvTable=
ConvTablePath=%_HOME%\Fichiers de ressources\Tables de conversion

[ModelOptions\Cld\ClssNamingOptions\ACDOBST\Code]
Template=
MaxLen=254
Case=M
ValidChar=&#39;a&#39;-&#39;z&#39;,&#39;A&#39;-&#39;Z&#39;,&#39;0&#39;-&#39;9&#39;,&quot;_&quot;
InvldChar=&quot; &#39;(.)+=*/&quot;
AllValid=Yes
NoAccent=Yes
DefaultChar=_
Script=.convert_code(%Code%,&quot; &quot;)
ConvTable=
ConvTablePath=%_HOME%\Fichiers de ressources\Tables de conversion

[ModelOptions\Cld\ClssNamingOptions\STAT]

[ModelOptions\Cld\ClssNamingOptions\STAT\Name]
Template=
MaxLen=254
Case=M
ValidChar=
InvldChar=
AllValid=Yes
NoAccent=No
DefaultChar=_
Script=.convert_name(%Name%,&quot;_&quot;)
ConvTable=
ConvTablePath=%_HOME%\Fichiers de ressources\Tables de conversion

[ModelOptions\Cld\ClssNamingOptions\STAT\Code]
Template=
MaxLen=254
Case=M
ValidChar=&#39;a&#39;-&#39;z&#39;,&#39;A&#39;-&#39;Z&#39;,&#39;0&#39;-&#39;9&#39;,&quot;_&quot;
InvldChar=&quot; &#39;(.)+=*/&quot;
AllValid=Yes
NoAccent=Yes
DefaultChar=_
Script=.convert_code(%Code%,&quot; &quot;)
ConvTable=
ConvTablePath=%_HOME%\Fichiers de ressources\Tables de conversion

[ModelOptions\Cld\ClssNamingOptions\DPDNODE]

[ModelOptions\Cld\ClssNamingOptions\DPDNODE\Name]
Template=
MaxLen=254
Case=M
ValidChar=
InvldChar=
AllValid=Yes
NoAccent=No
DefaultChar=_
Script=.convert_name(%Name%,&quot;_&quot;)
ConvTable=
ConvTablePath=%_HOME%\Fichiers de ressources\Tables de conversion

[ModelOptions\Cld\ClssNamingOptions\DPDNODE\Code]
Template=
MaxLen=254
Case=M
ValidChar=&#39;a&#39;-&#39;z&#39;,&#39;A&#39;-&#39;Z&#39;,&#39;0&#39;-&#39;9&#39;,&quot;_&quot;
InvldChar=&quot; &#39;(.)+=*/&quot;
AllValid=Yes
NoAccent=Yes
DefaultChar=_
Script=.convert_code(%Code%,&quot; &quot;)
ConvTable=
ConvTablePath=%_HOME%\Fichiers de ressources\Tables de conversion

[ModelOptions\Cld\ClssNamingOptions\DPDCMPI]

[ModelOptions\Cld\ClssNamingOptions\DPDCMPI\Name]
Template=
MaxLen=254
Case=M
ValidChar=
InvldChar=
AllValid=Yes
NoAccent=No
DefaultChar=_
Script=.convert_name(%Name%,&quot;_&quot;)
ConvTable=
ConvTablePath=%_HOME%\Fichiers de ressources\Tables de conversion

[ModelOptions\Cld\ClssNamingOptions\DPDCMPI\Code]
Template=
MaxLen=254
Case=M
ValidChar=&#39;a&#39;-&#39;z&#39;,&#39;A&#39;-&#39;Z&#39;,&#39;0&#39;-&#39;9&#39;,&quot;_&quot;
InvldChar=&quot; &#39;(.)+=*/&quot;
AllValid=Yes
NoAccent=Yes
DefaultChar=_
Script=.convert_code(%Code%,&quot; &quot;)
ConvTable=
ConvTablePath=%_HOME%\Fichiers de ressources\Tables de conversion

[ModelOptions\Cld\ClssNamingOptions\DPDASSC]

[ModelOptions\Cld\ClssNamingOptions\DPDASSC\Name]
Template=
MaxLen=254
Case=M
ValidChar=
InvldChar=
AllValid=Yes
NoAccent=No
DefaultChar=_
Script=.convert_name(%Name%,&quot;_&quot;)
ConvTable=
ConvTablePath=%_HOME%\Fichiers de ressources\Tables de conversion

[ModelOptions\Cld\ClssNamingOptions\DPDASSC\Code]
Template=
MaxLen=254
Case=M
ValidChar=&#39;a&#39;-&#39;z&#39;,&#39;A&#39;-&#39;Z&#39;,&#39;0&#39;-&#39;9&#39;,&quot;_&quot;
InvldChar=&quot; &#39;(.)+=*/&quot;
AllValid=Yes
NoAccent=Yes
DefaultChar=_
Script=.convert_code(%Code%,&quot; &quot;)
ConvTable=
ConvTablePath=%_HOME%\Fichiers de ressources\Tables de conversion

[ModelOptions\Cld\ClssNamingOptions\OOMVAR]

[ModelOptions\Cld\ClssNamingOptions\OOMVAR\Name]
Template=
MaxLen=254
Case=M
ValidChar=
InvldChar=
AllValid=Yes
NoAccent=No
DefaultChar=_
Script=.convert_name(%Name%,&quot;_&quot;)
ConvTable=
ConvTablePath=%_HOME%\Fichiers de ressources\Tables de conversion

[ModelOptions\Cld\ClssNamingOptions\OOMVAR\Code]
Template=
MaxLen=254
Case=M
ValidChar=&#39;a&#39;-&#39;z&#39;,&#39;A&#39;-&#39;Z&#39;,&#39;0&#39;-&#39;9&#39;,&quot;_&quot;
InvldChar=&quot; &#39;(.)+=*/&quot;
AllValid=Yes
NoAccent=Yes
DefaultChar=_
Script=.convert_code(%Code%,&quot; &quot;)
ConvTable=
ConvTablePath=%_HOME%\Fichiers de ressources\Tables de conversion

[ModelOptions\Cld\ClssNamingOptions\FILO]

[ModelOptions\Cld\ClssNamingOptions\FILO\Name]
Template=
MaxLen=254
Case=M
ValidChar=
InvldChar=&quot;\/:*?&lt;&gt;|&quot;
AllValid=Yes
NoAccent=No
DefaultChar=_
Script=.convert_name(%Name%,&quot;_&quot;)
ConvTable=
ConvTablePath=%_HOME%\Fichiers de ressources\Tables de conversion

[ModelOptions\Cld\ClssNamingOptions\FILO\Code]
Template=
MaxLen=254
Case=M
ValidChar=&#39;a&#39;-&#39;z&#39;,&#39;A&#39;-&#39;Z&#39;,&#39;0&#39;-&#39;9&#39;,&quot;_. &quot;
InvldChar=&quot; &#39;(.)+=*/&quot;
AllValid=Yes
NoAccent=Yes
DefaultChar=_
Script=.convert_code(%Code%,&quot; &quot;)
ConvTable=
ConvTablePath=%_HOME%\Fichiers de ressources\Tables de conversion

[ModelOptions\Cld\ClssNamingOptions\FRMEOBJ]

[ModelOptions\Cld\ClssNamingOptions\FRMEOBJ\Name]
Template=
MaxLen=254
Case=M
ValidChar=
InvldChar=
AllValid=Yes
NoAccent=No
DefaultChar=_
Script=.convert_name(%Name%,&quot;_&quot;)
ConvTable=
ConvTablePath=%_HOME%\Fichiers de ressources\Tables de conversion

[ModelOptions\Cld\ClssNamingOptions\FRMEOBJ\Code]
Template=
MaxLen=254
Case=M
ValidChar=&#39;a&#39;-&#39;z&#39;,&#39;A&#39;-&#39;Z&#39;,&#39;0&#39;-&#39;9&#39;,&quot;_&quot;
InvldChar=&quot; &#39;(.)+=*/&quot;
AllValid=Yes
NoAccent=Yes
DefaultChar=_
Script=.convert_code(%Code%,&quot; &quot;)
ConvTable=
ConvTablePath=%_HOME%\Fichiers de ressources\Tables de conversion

[ModelOptions\Cld\ClssNamingOptions\FRMELNK]

[ModelOptions\Cld\ClssNamingOptions\FRMELNK\Name]
Template=
MaxLen=254
Case=M
ValidChar=
InvldChar=
AllValid=Yes
NoAccent=No
DefaultChar=_
Script=.convert_name(%Name%,&quot;_&quot;)
ConvTable=
ConvTablePath=%_HOME%\Fichiers de ressources\Tables de conversion

[ModelOptions\Cld\ClssNamingOptions\FRMELNK\Code]
Template=
MaxLen=254
Case=M
ValidChar=&#39;a&#39;-&#39;z&#39;,&#39;A&#39;-&#39;Z&#39;,&#39;0&#39;-&#39;9&#39;,&quot;_&quot;
InvldChar=&quot; &#39;(.)+=*/&quot;
AllValid=Yes
NoAccent=Yes
DefaultChar=_
Script=.convert_code(%Code%,&quot; &quot;)
ConvTable=
ConvTablePath=%_HOME%\Fichiers de ressources\Tables de conversion

[ModelOptions\Cld\ClssNamingOptions\DefaultClass]

[ModelOptions\Cld\ClssNamingOptions\DefaultClass\Name]
Template=
MaxLen=254
Case=M
ValidChar=
InvldChar=
AllValid=Yes
NoAccent=No
DefaultChar=_
Script=.convert_name(%Name%,&quot;_&quot;)
ConvTable=
ConvTablePath=%_HOME%\Fichiers de ressources\Tables de conversion

[ModelOptions\Cld\ClssNamingOptions\DefaultClass\Code]
Template=
MaxLen=254
Case=M
ValidChar=&#39;a&#39;-&#39;z&#39;,&#39;A&#39;-&#39;Z&#39;,&#39;0&#39;-&#39;9&#39;,&quot;_&quot;
InvldChar=&quot; &#39;(.)+=*/&quot;
AllValid=Yes
NoAccent=Yes
DefaultChar=_
Script=.convert_code(%Code%,&quot; &quot;)
ConvTable=
ConvTablePath=%_HOME%\Fichiers de ressources\Tables de conversion

[ModelOptions\Generate]

[ModelOptions\Generate\Cdm]
CheckModel=Yes
SaveLinks=Yes
NameToCode=No
Notation=2

[ModelOptions\Generate\Pdm]
CheckModel=Yes
SaveLinks=Yes
ORMapping=No
NameToCode=No
BuildTrgr=No
TablePrefix=
RefrUpdRule=RESTRICT
RefrDelRule=RESTRICT
IndxPKName=%TABLE%_PK
IndxAKName=%TABLE%_AK
IndxFKName=%REFR%_FK
IndxThreshold=
ColnFKName=%.3:PARENT%_%COLUMN%
ColnFKNameUse=No

[ModelOptions\Generate\Xsm]
CheckModel=Yes
SaveLinks=Yes
ORMapping=No
NameToCode=No</a:ModelOptionsText>
<c:ObjectLanguage>
<o:Shortcut Id="o3">
<a:ObjectID>24E6A2F5-F589-43DC-B526-53967D32E75A</a:ObjectID>
<a:Name>Java</a:Name>
<a:Code>Java</a:Code>
<a:CreationDate>1767020302</a:CreationDate>
<a:Creator>houda</a:Creator>
<a:ModificationDate>1767020302</a:ModificationDate>
<a:Modifier>houda</a:Modifier>
<a:TargetStereotype/>
<a:TargetID>0DEDDB90-46E2-45A0-886E-411709DA0DC9</a:TargetID>
<a:TargetClassID>1811206C-1A4B-11D1-83D9-444553540000</a:TargetClassID>
</o:Shortcut>
</c:ObjectLanguage>
<c:ExtendedModelDefinitions>
<o:Shortcut Id="o4">
<a:ObjectID>7530CB06-D5D4-4742-961C-813DBFF4F279</a:ObjectID>
<a:Name>WSDL for Java</a:Name>
<a:Code>WSDLJava</a:Code>
<a:CreationDate>1767020303</a:CreationDate>
<a:Creator>houda</a:Creator>
<a:ModificationDate>1767020303</a:ModificationDate>
<a:Modifier>houda</a:Modifier>
<a:TargetStereotype/>
<a:TargetID>C8F5F7B2-CF9D-4E98-8301-959BB6E86C8A</a:TargetID>
<a:TargetClassID>186C8AC3-D3DC-11D3-881C-00508B03C75C</a:TargetClassID>
</o:Shortcut>
</c:ExtendedModelDefinitions>
<c:DefaultDiagram>
<o:UseCaseDiagram Ref="o5"/>
</c:DefaultDiagram>
<c:UseCaseDiagrams>
<o:UseCaseDiagram Id="o5">
<a:ObjectID>B2C00DCF-9CE1-4F63-B08B-1B655F6B53DB</a:ObjectID>
<a:Name>DiagrammeCasUtilisation_1</a:Name>
<a:Code>DiagrammeCasUtilisation_1</a:Code>
<a:CreationDate>1767020302</a:CreationDate>
<a:Creator>houda</a:Creator>
<a:ModificationDate>1767559223</a:ModificationDate>
<a:Modifier>houda</a:Modifier>
<a:DisplayPreferences>[DisplayPreferences]

[DisplayPreferences\UCD]

[DisplayPreferences\General]
Adjust to text=Yes
Snap Grid=No
Constrain Labels=Yes
Display Grid=No
Show Page Delimiter=Yes
Grid size=0
Graphic unit=2
Window color=255, 255, 255
Background image=
Background mode=8
Watermark image=
Watermark mode=8
Show watermark on screen=No
Gradient mode=0
Gradient end color=255, 255, 255
Show Swimlane=No
SwimlaneVert=Yes
TreeVert=No
CompDark=0

[DisplayPreferences\Object]
Mode=0
Trunc Length=80
Word Length=80
Word Text=!&quot;&quot;#$%&amp;&#39;()*+,-./:;&lt;=&gt;?@[\]^_`{|}~
Shortcut IntIcon=Yes
Shortcut IntLoct=Yes
Shortcut IntFullPath=No
Shortcut IntLastPackage=Yes
Shortcut ExtIcon=Yes
Shortcut ExtLoct=No
Shortcut ExtFullPath=No
Shortcut ExtLastPackage=Yes
Shortcut ExtIncludeModl=Yes
EObjShowStrn=Yes
ExtendedObject.Comment=No
ExtendedObject.IconPicture=No
ExtendedObject_SymbolLayout=
ELnkShowStrn=Yes
ELnkShowName=Yes
ExtendedLink_SymbolLayout=
FileObject.Stereotype=No
FileObject.DisplayName=Yes
FileObject.LocationOrName=No
FileObject.IconPicture=No
FileObject.IconMode=Yes
FileObject_SymbolLayout=
PckgShowStrn=Yes
Package.Comment=No
Package.IconPicture=No
Package_SymbolLayout=
Display Model Version=Yes
Actor.IconPicture=No
Actor_SymbolLayout=
UseCase.Stereotype=Yes
UseCase.Comment=No
UseCase.IconPicture=No
UseCase_SymbolLayout=&lt;Form&gt;[CRLF] &lt;StandardAttribute Name=&quot;Stéréotype&quot; Attribute=&quot;Stereotype&quot; Prefix=&quot;&amp;lt;&amp;lt;&quot; Suffix=&quot;&amp;gt;&amp;gt;&quot; Alignment=&quot;CNTR&quot; Caption=&quot;&quot; Mandatory=&quot;No&quot; /&gt;[CRLF] &lt;StandardAttribute Name=&quot;Nom&quot; Attribute=&quot;DisplayName&quot; Prefix=&quot;&quot; Suffix=&quot;&quot; Alignment=&quot;CNTR&quot; Caption=&quot;&quot; Mandatory=&quot;Yes&quot; /&gt;[CRLF] &lt;Separator Name=&quot;Séparateur&quot; /&gt;[CRLF] &lt;StandardAttribute Name=&quot;Commentaire&quot; Attribute=&quot;Comment&quot; Prefix=&quot;&quot; Suffix=&quot;&quot; Alignment=&quot;LEFT&quot; Caption=&quot;&quot; Mandatory=&quot;No&quot; /&gt;[CRLF] &lt;StandardAttribute Name=&quot;Icône&quot; Attribute=&quot;IconPicture&quot; Prefix=&quot;&quot; Suffix=&quot;&quot; Alignment=&quot;CNTR&quot; Caption=&quot;&quot; Mandatory=&quot;Yes&quot; /&gt;[CRLF]&lt;/Form&gt;
ActrShowStrn=Yes
AsscShowName=No
AsscShowDirt=No
AsscShowStrn=No
GnrlShowName=No
GnrlShowStrn=No
GnrlShowCntr=No
DepdShowName=No
DepdShowStrn=Yes
DepdShowCntr=No

[DisplayPreferences\Symbol]

[DisplayPreferences\Symbol\FRMEOBJ]
STRNFont=Arial,8,N
STRNFont color=0, 0, 0
DISPNAMEFont=Arial,8,N
DISPNAMEFont color=0, 0, 0
LABLFont=Arial,8,N
LABLFont color=0, 0, 0
AutoAdjustToText=Yes
Keep aspect=No
Keep center=No
Keep size=No
Width=6000
Height=2000
Brush color=255 255 255
Fill Color=Yes
Brush style=6
Brush bitmap mode=12
Brush gradient mode=64
Brush gradient color=192 192 192
Brush background image=
Custom shape=
Custom text mode=0
Pen=1 0 255 128 128
Shadow color=192 192 192
Shadow=0

[DisplayPreferences\Symbol\FRMELNK]
CENTERFont=Arial,8,N
CENTERFont color=0, 0, 0
Line style=2
AutoAdjustToText=Yes
Keep aspect=No
Keep center=No
Keep size=No
Brush color=255 255 255
Fill Color=Yes
Brush style=1
Brush bitmap mode=12
Brush gradient mode=0
Brush gradient color=118 118 118
Brush background image=
Custom shape=
Custom text mode=0
Pen=1 0 128 128 255
Shadow color=192 192 192
Shadow=0

[DisplayPreferences\Symbol\FILO]
OBJSTRNFont=Arial,8,N
OBJSTRNFont color=0, 0, 0
DISPNAMEFont=Arial,8,N
DISPNAMEFont color=0, 0, 0
LCNMFont=Arial,8,N
LCNMFont color=0, 0, 0
AutoAdjustToText=Yes
Keep aspect=Yes
Keep center=Yes
Keep size=No
Width=2400
Height=2400
Brush color=255 255 255
Fill Color=No
Brush style=1
Brush bitmap mode=12
Brush gradient mode=0
Brush gradient color=118 118 118
Brush background image=
Custom shape=
Custom text mode=0
Pen=1 0 0 0 255
Shadow color=192 192 192
Shadow=0

[DisplayPreferences\Symbol\CLDPCKG]
STRNFont=Arial,8,N
STRNFont color=0 0 0
DISPNAMEFont=Arial,8,N
DISPNAMEFont color=0 0 0
LABLFont=Arial,8,N
LABLFont color=0 0 0
AutoAdjustToText=Yes
Keep aspect=No
Keep center=No
Keep size=No
Width=4800
Height=3600
Brush color=255 255 192
Fill Color=Yes
Brush style=6
Brush bitmap mode=12
Brush gradient mode=65
Brush gradient color=255 255 255
Brush background image=
Custom shape=
Custom text mode=0
Pen=1 0 178 178 178
Shadow color=192 192 192
Shadow=0

[DisplayPreferences\Symbol\UCDACTR]
STRNFont=Arial,8,N
STRNFont color=0 0 0
DISPNAMEFont=Arial,8,N
DISPNAMEFont color=0 0 0
AutoAdjustToText=Yes
Keep aspect=Yes
Keep center=Yes
Keep size=No
Width=4800
Height=3600
Brush color=128 64 64
Fill Color=Yes
Brush style=6
Brush bitmap mode=12
Brush gradient mode=65
Brush gradient color=255 255 255
Brush background image=
Custom shape=
Custom text mode=0
Pen=1 150 128 0 0
Shadow color=192 192 192
Shadow=0

[DisplayPreferences\Symbol\UCDASSC]
DISPNAMEFont=Arial,8,N
DISPNAMEFont color=0 0 0
Line style=2
Pen=1 0 128 0 0
Shadow color=192 192 192
Shadow=0

[DisplayPreferences\Symbol\GNRLLINK]
DISPNAMEFont=Arial,8,N
DISPNAMEFont color=0 0 0
Line style=2
Pen=1 0 128 0 0
Shadow color=192 192 192
Shadow=0

[DisplayPreferences\Symbol\DEPDLINK]
DISPNAMEFont=Arial,8,N
DISPNAMEFont color=0 0 0
Line style=2
Pen=2 0 128 0 0
Shadow color=192 192 192
Shadow=0

[DisplayPreferences\Symbol\UCDUCAS]
STRNFont=Arial,8,N
STRNFont color=0 0 0
DISPNAMEFont=Arial,8,N
DISPNAMEFont color=0 0 0
LABLFont=Arial,8,N
LABLFont color=0 0 0
AutoAdjustToText=Yes
Keep aspect=No
Keep center=No
Keep size=No
Width=7200
Height=5400
Brush color=255 207 159
Fill Color=Yes
Brush style=6
Brush bitmap mode=12
Brush gradient mode=16
Brush gradient color=255 255 255
Brush background image=
Custom shape=
Custom text mode=0
Pen=1 150 128 0 0
Shadow color=192 192 192
Shadow=0

[DisplayPreferences\Symbol\USRDEPD]
OBJXSTRFont=Arial,8,N
OBJXSTRFont color=0 0 0
Line style=2
AutoAdjustToText=Yes
Keep aspect=No
Keep center=No
Keep size=No
Brush color=255 255 255
Fill Color=Yes
Brush style=1
Brush bitmap mode=12
Brush gradient mode=0
Brush gradient color=118 118 118
Brush background image=
Custom shape=
Custom text mode=0
Pen=2 0 128 0 0
Shadow color=192 192 192
Shadow=0

[DisplayPreferences\Symbol\Free Symbol]
Free TextFont=Arial,8,N
Free TextFont color=0 0 0
Line style=2
AutoAdjustToText=Yes
Keep aspect=No
Keep center=No
Keep size=No
Brush color=255 255 255
Fill Color=Yes
Brush style=1
Brush bitmap mode=12
Brush gradient mode=0
Brush gradient color=118 118 118
Brush background image=
Custom shape=
Custom text mode=0
Pen=1 0 128 0 0
Shadow color=192 192 192
Shadow=0</a:DisplayPreferences>
<a:PaperSize>(8268, 11693)</a:PaperSize>
<a:PageMargins>((315,354), (433,354))</a:PageMargins>
<a:PageOrientation>1</a:PageOrientation>
<a:PaperSource>15</a:PaperSource>
<c:Symbols>
<o:DependencySymbol Id="o6">
<a:CreationDate>1767558918</a:CreationDate>
<a:ModificationDate>1767558918</a:ModificationDate>
<a:Rect>((25666,4138), (27016,12313))</a:Rect>
<a:ListOfPoints>((25666,4138),(25666,8287),(27016,8287),(27016,12313))</a:ListOfPoints>
<a:CornerStyle>2</a:CornerStyle>
<a:ArrowStyle>8</a:ArrowStyle>
<a:LineColor>128</a:LineColor>
<a:DashStyle>2</a:DashStyle>
<a:ShadowColor>12632256</a:ShadowColor>
<a:FontList>DISPNAME 0 Arial,8,N</a:FontList>
<c:SourceSymbol>
<o:UseCaseSymbol Ref="o7"/>
</c:SourceSymbol>
<c:DestinationSymbol>
<o:UseCaseSymbol Ref="o8"/>
</c:DestinationSymbol>
<c:Object>
<o:Dependency Ref="o9"/>
</c:Object>
</o:DependencySymbol>
<o:DependencySymbol Id="o10">
<a:CreationDate>1767559042</a:CreationDate>
<a:ModificationDate>1767559081</a:ModificationDate>
<a:Rect>((-34902,-26948), (-33574,-21391))</a:Rect>
<a:ListOfPoints>((-34902,-21391),(-34902,-24139),(-33574,-24139),(-33574,-26948))</a:ListOfPoints>
<a:CornerStyle>2</a:CornerStyle>
<a:ArrowStyle>8</a:ArrowStyle>
<a:LineColor>128</a:LineColor>
<a:DashStyle>2</a:DashStyle>
<a:ShadowColor>12632256</a:ShadowColor>
<a:FontList>DISPNAME 0 Arial,8,N</a:FontList>
<c:SourceSymbol>
<o:UseCaseSymbol Ref="o11"/>
</c:SourceSymbol>
<c:DestinationSymbol>
<o:UseCaseSymbol Ref="o12"/>
</c:DestinationSymbol>
<c:Object>
<o:Dependency Ref="o13"/>
</c:Object>
</o:DependencySymbol>
<o:RectangleSymbol Id="o14">
<a:CreationDate>1767532560</a:CreationDate>
<a:ModificationDate>1767533982</a:ModificationDate>
<a:Rect>((-16497,39901), (20179,22951))</a:Rect>
<a:TextStyle>4130</a:TextStyle>
<a:AutoAdjustToText>0</a:AutoAdjustToText>
<a:LineColor>128</a:LineColor>
<a:FillColor>16777215</a:FillColor>
<a:ShadowColor>12632256</a:ShadowColor>
<a:FontName>Arial,8,N</a:FontName>
<a:ManuallyResized>1</a:ManuallyResized>
</o:RectangleSymbol>
<o:TextSymbol Id="o15">
<a:Text>Gestion de profile</a:Text>
<a:CreationDate>1767532576</a:CreationDate>
<a:ModificationDate>1767532601</a:ModificationDate>
<a:Rect>((-6989,39600), (13336,38325))</a:Rect>
<a:TextStyle>4130</a:TextStyle>
<a:LineColor>0</a:LineColor>
<a:DashStyle>7</a:DashStyle>
<a:FillColor>0</a:FillColor>
<a:ShadowColor>12632256</a:ShadowColor>
<a:FontName>Arial,8,N</a:FontName>
</o:TextSymbol>
<o:RectangleSymbol Id="o16">
<a:CreationDate>1767532793</a:CreationDate>
<a:ModificationDate>1767559085</a:ModificationDate>
<a:Rect>((-42266,-8104), (-25964,-30934))</a:Rect>
<a:TextStyle>4130</a:TextStyle>
<a:AutoAdjustToText>0</a:AutoAdjustToText>
<a:LineColor>128</a:LineColor>
<a:FillColor>16777215</a:FillColor>
<a:ShadowColor>12632256</a:ShadowColor>
<a:FontName>Arial,8,N</a:FontName>
<a:ManuallyResized>1</a:ManuallyResized>
</o:RectangleSymbol>
<o:TextSymbol Id="o17">
<a:Text>Gestion des donnees</a:Text>
<a:CreationDate>1767533059</a:CreationDate>
<a:ModificationDate>1767559073</a:ModificationDate>
<a:Rect>((-40259,-6344), (-27809,-13598))</a:Rect>
<a:TextStyle>4130</a:TextStyle>
<a:AutoAdjustToText>0</a:AutoAdjustToText>
<a:LineColor>0</a:LineColor>
<a:DashStyle>7</a:DashStyle>
<a:FillColor>0</a:FillColor>
<a:ShadowColor>12632256</a:ShadowColor>
<a:FontName>Arial,8,N</a:FontName>
<a:ManuallyResized>1</a:ManuallyResized>
</o:TextSymbol>
<o:DependencySymbol Id="o18">
<a:CreationDate>1767532491</a:CreationDate>
<a:ModificationDate>1767532722</a:ModificationDate>
<a:Rect>((26011,4500), (27886,11850))</a:Rect>
<a:ListOfPoints>((27886,4500),(27886,10087),(26011,10087),(26011,11850))</a:ListOfPoints>
<a:CornerStyle>2</a:CornerStyle>
<a:ArrowStyle>8</a:ArrowStyle>
<a:LineColor>128</a:LineColor>
<a:DashStyle>2</a:DashStyle>
<a:ShadowColor>12632256</a:ShadowColor>
<a:FontList>DISPNAME 0 Arial,8,N</a:FontList>
<c:SourceSymbol>
<o:UseCaseSymbol Ref="o7"/>
</c:SourceSymbol>
<c:DestinationSymbol>
<o:UseCaseSymbol Ref="o8"/>
</c:DestinationSymbol>
<c:Object>
<o:Dependency Ref="o19"/>
</c:Object>
</o:DependencySymbol>
<o:DependencySymbol Id="o20">
<a:CreationDate>1767532495</a:CreationDate>
<a:ModificationDate>1767532722</a:ModificationDate>
<a:Rect>((27849,4200), (28449,12000))</a:Rect>
<a:ListOfPoints>((27961,12000),(27961,10087),(28336,10087),(28336,4200))</a:ListOfPoints>
<a:CornerStyle>2</a:CornerStyle>
<a:ArrowStyle>8</a:ArrowStyle>
<a:LineColor>128</a:LineColor>
<a:DashStyle>2</a:DashStyle>
<a:ShadowColor>12632256</a:ShadowColor>
<a:FontList>DISPNAME 0 Arial,8,N</a:FontList>
<c:SourceSymbol>
<o:UseCaseSymbol Ref="o8"/>
</c:SourceSymbol>
<c:DestinationSymbol>
<o:UseCaseSymbol Ref="o7"/>
</c:DestinationSymbol>
<c:Object>
<o:Dependency Ref="o21"/>
</c:Object>
</o:DependencySymbol>
<o:RectangleSymbol Id="o22">
<a:CreationDate>1767531611</a:CreationDate>
<a:ModificationDate>1767532666</a:ModificationDate>
<a:Rect>((-6989,-42299), (40763,-63225))</a:Rect>
<a:TextStyle>4130</a:TextStyle>
<a:AutoAdjustToText>0</a:AutoAdjustToText>
<a:LineColor>128</a:LineColor>
<a:FillColor>16777215</a:FillColor>
<a:ShadowColor>12632256</a:ShadowColor>
<a:FontName>Arial,8,N</a:FontName>
<a:ManuallyResized>1</a:ManuallyResized>
</o:RectangleSymbol>
<o:TextSymbol Id="o23">
<a:Text>ANALYSE DE CROISSANCE</a:Text>
<a:CreationDate>1767531826</a:CreationDate>
<a:ModificationDate>1767532688</a:ModificationDate>
<a:Rect>((11971,-42525), (27796,-44550))</a:Rect>
<a:TextStyle>4130</a:TextStyle>
<a:LineColor>0</a:LineColor>
<a:DashStyle>7</a:DashStyle>
<a:FillColor>0</a:FillColor>
<a:ShadowColor>12632256</a:ShadowColor>
<a:FontName>Arial,8,N</a:FontName>
</o:TextSymbol>
<o:RectangleSymbol Id="o24">
<a:CreationDate>1767531959</a:CreationDate>
<a:ModificationDate>1767534463</a:ModificationDate>
<a:Rect>((-52739,-47175), (-11278,-64350))</a:Rect>
<a:TextStyle>4130</a:TextStyle>
<a:AutoAdjustToText>0</a:AutoAdjustToText>
<a:LineColor>128</a:LineColor>
<a:FillColor>16777215</a:FillColor>
<a:ShadowColor>12632256</a:ShadowColor>
<a:FontName>Arial,8,N</a:FontName>
</o:RectangleSymbol>
<o:TextSymbol Id="o25">
<a:Text>Assistance IA</a:Text>
<a:CreationDate>1767531976</a:CreationDate>
<a:ModificationDate>1767532684</a:ModificationDate>
<a:Rect>((-39553,-47250), (-26728,-48675))</a:Rect>
<a:TextStyle>4130</a:TextStyle>
<a:LineColor>0</a:LineColor>
<a:DashStyle>7</a:DashStyle>
<a:FillColor>0</a:FillColor>
<a:ShadowColor>12632256</a:ShadowColor>
<a:FontName>Arial,8,N</a:FontName>
</o:TextSymbol>
<o:RectangleSymbol Id="o26">
<a:CreationDate>1767532202</a:CreationDate>
<a:ModificationDate>1767532202</a:ModificationDate>
<a:Rect>((-7903,-4125), (35447,-36225))</a:Rect>
<a:TextStyle>4130</a:TextStyle>
<a:AutoAdjustToText>0</a:AutoAdjustToText>
<a:LineColor>128</a:LineColor>
<a:FillColor>16777215</a:FillColor>
<a:ShadowColor>12632256</a:ShadowColor>
<a:FontName>Arial,8,N</a:FontName>
</o:RectangleSymbol>
<o:TextSymbol Id="o27">
<a:Text>Gestion de quotidien</a:Text>
<a:CreationDate>1767532268</a:CreationDate>
<a:ModificationDate>1767532299</a:ModificationDate>
<a:Rect>((7486,-4425), (21136,-5850))</a:Rect>
<a:TextStyle>4130</a:TextStyle>
<a:LineColor>0</a:LineColor>
<a:DashStyle>7</a:DashStyle>
<a:FillColor>0</a:FillColor>
<a:ShadowColor>12632256</a:ShadowColor>
<a:FontName>Arial,8,N</a:FontName>
</o:TextSymbol>
<o:RectangleSymbol Id="o28">
<a:CreationDate>1767532408</a:CreationDate>
<a:ModificationDate>1767532738</a:ModificationDate>
<a:Rect>((-10046,21375), (38011,-3075))</a:Rect>
<a:TextStyle>4130</a:TextStyle>
<a:AutoAdjustToText>0</a:AutoAdjustToText>
<a:LineColor>128</a:LineColor>
<a:FillColor>16777215</a:FillColor>
<a:ShadowColor>12632256</a:ShadowColor>
<a:FontName>Arial,8,N</a:FontName>
<a:ManuallyResized>1</a:ManuallyResized>
</o:RectangleSymbol>
<o:TextSymbol Id="o29">
<a:Text>Suivre Sante</a:Text>
<a:CreationDate>1767532417</a:CreationDate>
<a:ModificationDate>1767532438</a:ModificationDate>
<a:Rect>((5161,21525), (19111,19125))</a:Rect>
<a:TextStyle>4130</a:TextStyle>
<a:LineColor>0</a:LineColor>
<a:DashStyle>7</a:DashStyle>
<a:FillColor>0</a:FillColor>
<a:ShadowColor>12632256</a:ShadowColor>
<a:FontName>Arial,8,N</a:FontName>
</o:TextSymbol>
<o:GeneralizationSymbol Id="o30">
<a:CreationDate>1767370603</a:CreationDate>
<a:ModificationDate>1767532735</a:ModificationDate>
<a:Rect>((-908,10837), (23363,12824))</a:Rect>
<a:ListOfPoints>((23363,12824),(3680,12824),(3680,10837),(-908,10837))</a:ListOfPoints>
<a:CornerStyle>2</a:CornerStyle>
<a:ArrowStyle>7</a:ArrowStyle>
<a:LineColor>128</a:LineColor>
<a:ShadowColor>12632256</a:ShadowColor>
<a:FontList>DISPNAME 0 Arial,8,N</a:FontList>
<c:SourceSymbol>
<o:UseCaseSymbol Ref="o8"/>
</c:SourceSymbol>
<c:DestinationSymbol>
<o:UseCaseSymbol Ref="o31"/>
</c:DestinationSymbol>
<c:Object>
<o:Generalization Ref="o32"/>
</c:Object>
</o:GeneralizationSymbol>
<o:GeneralizationSymbol Id="o33">
<a:CreationDate>1767370605</a:CreationDate>
<a:ModificationDate>1767532735</a:ModificationDate>
<a:Rect>((146,4200), (21413,10688))</a:Rect>
<a:ListOfPoints>((21413,4200),(21413,10688),(146,10688))</a:ListOfPoints>
<a:CornerStyle>2</a:CornerStyle>
<a:ArrowStyle>7</a:ArrowStyle>
<a:LineColor>128</a:LineColor>
<a:ShadowColor>12632256</a:ShadowColor>
<a:FontList>DISPNAME 0 Arial,8,N</a:FontList>
<c:SourceSymbol>
<o:UseCaseSymbol Ref="o7"/>
</c:SourceSymbol>
<c:DestinationSymbol>
<o:UseCaseSymbol Ref="o31"/>
</c:DestinationSymbol>
<c:Object>
<o:Generalization Ref="o34"/>
</c:Object>
</o:GeneralizationSymbol>
<o:GeneralizationSymbol Id="o35">
<a:CreationDate>1767370607</a:CreationDate>
<a:ModificationDate>1767532735</a:ModificationDate>
<a:Rect>((-880,-525), (14888,10463))</a:Rect>
<a:ListOfPoints>((14888,-525),(14888,10463),(-880,10463))</a:ListOfPoints>
<a:CornerStyle>2</a:CornerStyle>
<a:ArrowStyle>7</a:ArrowStyle>
<a:LineColor>128</a:LineColor>
<a:ShadowColor>12632256</a:ShadowColor>
<a:FontList>DISPNAME 0 Arial,8,N</a:FontList>
<c:SourceSymbol>
<o:UseCaseSymbol Ref="o36"/>
</c:SourceSymbol>
<c:DestinationSymbol>
<o:UseCaseSymbol Ref="o31"/>
</c:DestinationSymbol>
<c:Object>
<o:Generalization Ref="o37"/>
</c:Object>
</o:GeneralizationSymbol>
<o:GeneralizationSymbol Id="o38">
<a:CreationDate>1767370610</a:CreationDate>
<a:ModificationDate>1767532735</a:ModificationDate>
<a:Rect>((-2887,1125), (-1286,10688))</a:Rect>
<a:ListOfPoints>((-2887,1125),(-2887,6919),(-1286,6919),(-1286,10688))</a:ListOfPoints>
<a:CornerStyle>2</a:CornerStyle>
<a:ArrowStyle>7</a:ArrowStyle>
<a:LineColor>128</a:LineColor>
<a:ShadowColor>12632256</a:ShadowColor>
<a:FontList>DISPNAME 0 Arial,8,N</a:FontList>
<c:SourceSymbol>
<o:UseCaseSymbol Ref="o39"/>
</c:SourceSymbol>
<c:DestinationSymbol>
<o:UseCaseSymbol Ref="o31"/>
</c:DestinationSymbol>
<c:Object>
<o:Generalization Ref="o40"/>
</c:Object>
</o:GeneralizationSymbol>
<o:GeneralizationSymbol Id="o41">
<a:CreationDate>1767370664</a:CreationDate>
<a:ModificationDate>1767532735</a:ModificationDate>
<a:Rect>((828,10613), (9488,16575))</a:Rect>
<a:ListOfPoints>((9488,16575),(9488,10613),(828,10613))</a:ListOfPoints>
<a:CornerStyle>2</a:CornerStyle>
<a:ArrowStyle>7</a:ArrowStyle>
<a:LineColor>128</a:LineColor>
<a:ShadowColor>12632256</a:ShadowColor>
<a:FontList>DISPNAME 0 Arial,8,N</a:FontList>
<c:SourceSymbol>
<o:UseCaseSymbol Ref="o42"/>
</c:SourceSymbol>
<c:DestinationSymbol>
<o:UseCaseSymbol Ref="o31"/>
</c:DestinationSymbol>
<c:Object>
<o:Generalization Ref="o43"/>
</c:Object>
</o:GeneralizationSymbol>
<o:GeneralizationSymbol Id="o44">
<a:CreationDate>1767373301</a:CreationDate>
<a:ModificationDate>1767532611</a:ModificationDate>
<a:Rect>((-9044,33995), (9135,34995))</a:Rect>
<a:ListOfPoints>((9135,34495),(-9044,34495))</a:ListOfPoints>
<a:CornerStyle>2</a:CornerStyle>
<a:ArrowStyle>7</a:ArrowStyle>
<a:LineColor>128</a:LineColor>
<a:ShadowColor>12632256</a:ShadowColor>
<a:FontList>DISPNAME 0 Arial,8,N</a:FontList>
<c:SourceSymbol>
<o:UseCaseSymbol Ref="o45"/>
</c:SourceSymbol>
<c:DestinationSymbol>
<o:UseCaseSymbol Ref="o46"/>
</c:DestinationSymbol>
<c:Object>
<o:Generalization Ref="o47"/>
</c:Object>
</o:GeneralizationSymbol>
<o:GeneralizationSymbol Id="o48">
<a:CreationDate>1767373305</a:CreationDate>
<a:ModificationDate>1767532607</a:ModificationDate>
<a:Rect>((-9044,27539), (-5077,33517))</a:Rect>
<a:ListOfPoints>((-5077,27539),(-5077,33517),(-9044,33517))</a:ListOfPoints>
<a:CornerStyle>2</a:CornerStyle>
<a:ArrowStyle>7</a:ArrowStyle>
<a:LineColor>128</a:LineColor>
<a:ShadowColor>12632256</a:ShadowColor>
<a:FontList>DISPNAME 0 Arial,8,N</a:FontList>
<c:SourceSymbol>
<o:UseCaseSymbol Ref="o49"/>
</c:SourceSymbol>
<c:DestinationSymbol>
<o:UseCaseSymbol Ref="o46"/>
</c:DestinationSymbol>
<c:Object>
<o:Generalization Ref="o50"/>
</c:Object>
</o:GeneralizationSymbol>
<o:GeneralizationSymbol Id="o51">
<a:CreationDate>1767373307</a:CreationDate>
<a:ModificationDate>1767532609</a:ModificationDate>
<a:Rect>((-8969,27765), (6885,33315))</a:Rect>
<a:ListOfPoints>((6885,27765),(6885,33315),(-8969,33315))</a:ListOfPoints>
<a:CornerStyle>2</a:CornerStyle>
<a:ArrowStyle>7</a:ArrowStyle>
<a:LineColor>128</a:LineColor>
<a:ShadowColor>12632256</a:ShadowColor>
<a:FontList>DISPNAME 0 Arial,8,N</a:FontList>
<c:SourceSymbol>
<o:UseCaseSymbol Ref="o52"/>
</c:SourceSymbol>
<c:DestinationSymbol>
<o:UseCaseSymbol Ref="o46"/>
</c:DestinationSymbol>
<c:Object>
<o:Generalization Ref="o53"/>
</c:Object>
</o:GeneralizationSymbol>
<o:GeneralizationSymbol Id="o54">
<a:CreationDate>1767373839</a:CreationDate>
<a:ModificationDate>1767375813</a:ModificationDate>
<a:Rect>((-486,-20444), (6796,-9060))</a:Rect>
<a:ListOfPoints>((6796,-9060),(6796,-13300),(-486,-13300),(-486,-20444))</a:ListOfPoints>
<a:CornerStyle>2</a:CornerStyle>
<a:ArrowStyle>7</a:ArrowStyle>
<a:LineColor>128</a:LineColor>
<a:ShadowColor>12632256</a:ShadowColor>
<a:FontList>DISPNAME 0 Arial,8,N</a:FontList>
<c:SourceSymbol>
<o:UseCaseSymbol Ref="o55"/>
</c:SourceSymbol>
<c:DestinationSymbol>
<o:UseCaseSymbol Ref="o56"/>
</c:DestinationSymbol>
<c:Object>
<o:Generalization Ref="o57"/>
</c:Object>
</o:GeneralizationSymbol>
<o:GeneralizationSymbol Id="o58">
<a:CreationDate>1767373841</a:CreationDate>
<a:ModificationDate>1767375813</a:ModificationDate>
<a:Rect>((1164,-20444), (6135,-17392))</a:Rect>
<a:ListOfPoints>((6135,-17392),(6135,-20444),(1164,-20444))</a:ListOfPoints>
<a:CornerStyle>2</a:CornerStyle>
<a:ArrowStyle>7</a:ArrowStyle>
<a:LineColor>128</a:LineColor>
<a:ShadowColor>12632256</a:ShadowColor>
<a:FontList>DISPNAME 0 Arial,8,N</a:FontList>
<c:SourceSymbol>
<o:UseCaseSymbol Ref="o59"/>
</c:SourceSymbol>
<c:DestinationSymbol>
<o:UseCaseSymbol Ref="o56"/>
</c:DestinationSymbol>
<c:Object>
<o:Generalization Ref="o60"/>
</c:Object>
</o:GeneralizationSymbol>
<o:GeneralizationSymbol Id="o61">
<a:CreationDate>1767373848</a:CreationDate>
<a:ModificationDate>1767375813</a:ModificationDate>
<a:Rect>((39,-24765), (4215,-20594))</a:Rect>
<a:ListOfPoints>((4215,-24765),(39,-24765),(39,-20594))</a:ListOfPoints>
<a:CornerStyle>2</a:CornerStyle>
<a:ArrowStyle>7</a:ArrowStyle>
<a:LineColor>128</a:LineColor>
<a:ShadowColor>12632256</a:ShadowColor>
<a:FontList>DISPNAME 0 Arial,8,N</a:FontList>
<c:SourceSymbol>
<o:UseCaseSymbol Ref="o62"/>
</c:SourceSymbol>
<c:DestinationSymbol>
<o:UseCaseSymbol Ref="o56"/>
</c:DestinationSymbol>
<c:Object>
<o:Generalization Ref="o63"/>
</c:Object>
</o:GeneralizationSymbol>
<o:GeneralizationSymbol Id="o64">
<a:CreationDate>1767373887</a:CreationDate>
<a:ModificationDate>1767375754</a:ModificationDate>
<a:Rect>((9871,-8555), (16013,-7555))</a:Rect>
<a:ListOfPoints>((16013,-8055),(9871,-8055))</a:ListOfPoints>
<a:CornerStyle>2</a:CornerStyle>
<a:ArrowStyle>7</a:ArrowStyle>
<a:LineColor>128</a:LineColor>
<a:ShadowColor>12632256</a:ShadowColor>
<a:FontList>DISPNAME 0 Arial,8,N</a:FontList>
<c:SourceSymbol>
<o:UseCaseSymbol Ref="o65"/>
</c:SourceSymbol>
<c:DestinationSymbol>
<o:UseCaseSymbol Ref="o55"/>
</c:DestinationSymbol>
<c:Object>
<o:Generalization Ref="o66"/>
</c:Object>
</o:GeneralizationSymbol>
<o:GeneralizationSymbol Id="o67">
<a:CreationDate>1767373899</a:CreationDate>
<a:ModificationDate>1767375754</a:ModificationDate>
<a:Rect>((10771,-11700), (16088,-8160))</a:Rect>
<a:ListOfPoints>((16088,-11700),(10771,-11700),(10771,-8160))</a:ListOfPoints>
<a:CornerStyle>2</a:CornerStyle>
<a:ArrowStyle>7</a:ArrowStyle>
<a:LineColor>128</a:LineColor>
<a:ShadowColor>12632256</a:ShadowColor>
<a:FontList>DISPNAME 0 Arial,8,N</a:FontList>
<c:SourceSymbol>
<o:UseCaseSymbol Ref="o68"/>
</c:SourceSymbol>
<c:DestinationSymbol>
<o:UseCaseSymbol Ref="o55"/>
</c:DestinationSymbol>
<c:Object>
<o:Generalization Ref="o69"/>
</c:Object>
</o:GeneralizationSymbol>
<o:GeneralizationSymbol Id="o70">
<a:CreationDate>1767373903</a:CreationDate>
<a:ModificationDate>1767375755</a:ModificationDate>
<a:Rect>((8535,-17258), (15938,-16258))</a:Rect>
<a:ListOfPoints>((15938,-16758),(8535,-16758))</a:ListOfPoints>
<a:CornerStyle>2</a:CornerStyle>
<a:ArrowStyle>7</a:ArrowStyle>
<a:LineColor>128</a:LineColor>
<a:ShadowColor>12632256</a:ShadowColor>
<a:FontList>DISPNAME 0 Arial,8,N</a:FontList>
<c:SourceSymbol>
<o:UseCaseSymbol Ref="o71"/>
</c:SourceSymbol>
<c:DestinationSymbol>
<o:UseCaseSymbol Ref="o59"/>
</c:DestinationSymbol>
<c:Object>
<o:Generalization Ref="o72"/>
</c:Object>
</o:GeneralizationSymbol>
<o:GeneralizationSymbol Id="o73">
<a:CreationDate>1767373904</a:CreationDate>
<a:ModificationDate>1767375755</a:ModificationDate>
<a:Rect>((10185,-20475), (12788,-16193))</a:Rect>
<a:ListOfPoints>((12788,-20475),(12788,-16193),(10185,-16193))</a:ListOfPoints>
<a:CornerStyle>2</a:CornerStyle>
<a:ArrowStyle>7</a:ArrowStyle>
<a:LineColor>128</a:LineColor>
<a:ShadowColor>12632256</a:ShadowColor>
<a:FontList>DISPNAME 0 Arial,8,N</a:FontList>
<c:SourceSymbol>
<o:UseCaseSymbol Ref="o74"/>
</c:SourceSymbol>
<c:DestinationSymbol>
<o:UseCaseSymbol Ref="o59"/>
</c:DestinationSymbol>
<c:Object>
<o:Generalization Ref="o75"/>
</c:Object>
</o:GeneralizationSymbol>
<o:GeneralizationSymbol Id="o76">
<a:CreationDate>1767373906</a:CreationDate>
<a:ModificationDate>1767375757</a:ModificationDate>
<a:Rect>((9240,-25670), (13913,-24670))</a:Rect>
<a:ListOfPoints>((13913,-25170),(9240,-25170))</a:ListOfPoints>
<a:CornerStyle>2</a:CornerStyle>
<a:ArrowStyle>7</a:ArrowStyle>
<a:LineColor>128</a:LineColor>
<a:ShadowColor>12632256</a:ShadowColor>
<a:FontList>DISPNAME 0 Arial,8,N</a:FontList>
<c:SourceSymbol>
<o:UseCaseSymbol Ref="o77"/>
</c:SourceSymbol>
<c:DestinationSymbol>
<o:UseCaseSymbol Ref="o62"/>
</c:DestinationSymbol>
<c:Object>
<o:Generalization Ref="o78"/>
</c:Object>
</o:GeneralizationSymbol>
<o:GeneralizationSymbol Id="o79">
<a:CreationDate>1767373909</a:CreationDate>
<a:ModificationDate>1767375757</a:ModificationDate>
<a:Rect>((10215,-31875), (12713,-24240))</a:Rect>
<a:ListOfPoints>((12713,-31875),(12713,-28056),(10215,-28056),(10215,-24240))</a:ListOfPoints>
<a:CornerStyle>2</a:CornerStyle>
<a:ArrowStyle>7</a:ArrowStyle>
<a:LineColor>128</a:LineColor>
<a:ShadowColor>12632256</a:ShadowColor>
<a:FontList>DISPNAME 0 Arial,8,N</a:FontList>
<c:SourceSymbol>
<o:UseCaseSymbol Ref="o80"/>
</c:SourceSymbol>
<c:DestinationSymbol>
<o:UseCaseSymbol Ref="o62"/>
</c:DestinationSymbol>
<c:Object>
<o:Generalization Ref="o81"/>
</c:Object>
</o:GeneralizationSymbol>
<o:GeneralizationSymbol Id="o82">
<a:CreationDate>1767374529</a:CreationDate>
<a:ModificationDate>1767532677</a:ModificationDate>
<a:Rect>((11446,-60429), (24616,-52704))</a:Rect>
<a:ListOfPoints>((24616,-60429),(24616,-52704),(11446,-52704))</a:ListOfPoints>
<a:CornerStyle>2</a:CornerStyle>
<a:ArrowStyle>7</a:ArrowStyle>
<a:LineColor>128</a:LineColor>
<a:ShadowColor>12632256</a:ShadowColor>
<a:FontList>DISPNAME 0 Arial,8,N</a:FontList>
<c:SourceSymbol>
<o:UseCaseSymbol Ref="o83"/>
</c:SourceSymbol>
<c:DestinationSymbol>
<o:UseCaseSymbol Ref="o84"/>
</c:DestinationSymbol>
<c:Object>
<o:Generalization Ref="o85"/>
</c:Object>
</o:GeneralizationSymbol>
<o:GeneralizationSymbol Id="o86">
<a:CreationDate>1767374535</a:CreationDate>
<a:ModificationDate>1767532674</a:ModificationDate>
<a:Rect>((14655,-52467), (25980,-47967))</a:Rect>
<a:ListOfPoints>((25980,-47967),(20918,-47967),(20918,-52467),(14655,-52467))</a:ListOfPoints>
<a:CornerStyle>2</a:CornerStyle>
<a:ArrowStyle>7</a:ArrowStyle>
<a:LineColor>128</a:LineColor>
<a:ShadowColor>12632256</a:ShadowColor>
<a:FontList>DISPNAME 0 Arial,8,N</a:FontList>
<c:SourceSymbol>
<o:UseCaseSymbol Ref="o87"/>
</c:SourceSymbol>
<c:DestinationSymbol>
<o:UseCaseSymbol Ref="o84"/>
</c:DestinationSymbol>
<c:Object>
<o:Generalization Ref="o88"/>
</c:Object>
</o:GeneralizationSymbol>
<o:GeneralizationSymbol Id="o89">
<a:CreationDate>1767374539</a:CreationDate>
<a:ModificationDate>1767532675</a:ModificationDate>
<a:Rect>((5715,-53707), (25223,-52707))</a:Rect>
<a:ListOfPoints>((25223,-53207),(5715,-53207))</a:ListOfPoints>
<a:CornerStyle>2</a:CornerStyle>
<a:ArrowStyle>7</a:ArrowStyle>
<a:LineColor>128</a:LineColor>
<a:ShadowColor>12632256</a:ShadowColor>
<a:FontList>DISPNAME 0 Arial,8,N</a:FontList>
<c:SourceSymbol>
<o:UseCaseSymbol Ref="o90"/>
</c:SourceSymbol>
<c:DestinationSymbol>
<o:UseCaseSymbol Ref="o84"/>
</c:DestinationSymbol>
<c:Object>
<o:Generalization Ref="o91"/>
</c:Object>
</o:GeneralizationSymbol>
<o:GeneralizationSymbol Id="o92">
<a:CreationDate>1767374722</a:CreationDate>
<a:ModificationDate>1767532697</a:ModificationDate>
<a:Rect>((-43724,-61405), (-27644,-56455))</a:Rect>
<a:ListOfPoints>((-27644,-61405),(-27644,-56455),(-43724,-56455))</a:ListOfPoints>
<a:CornerStyle>2</a:CornerStyle>
<a:ArrowStyle>7</a:ArrowStyle>
<a:LineColor>128</a:LineColor>
<a:ShadowColor>12632256</a:ShadowColor>
<a:FontList>DISPNAME 0 Arial,8,N</a:FontList>
<c:SourceSymbol>
<o:UseCaseSymbol Ref="o93"/>
</c:SourceSymbol>
<c:DestinationSymbol>
<o:UseCaseSymbol Ref="o94"/>
</c:DestinationSymbol>
<c:Object>
<o:Generalization Ref="o95"/>
</c:Object>
</o:GeneralizationSymbol>
<o:GeneralizationSymbol Id="o96">
<a:CreationDate>1767374725</a:CreationDate>
<a:ModificationDate>1767532694</a:ModificationDate>
<a:Rect>((-40837,-56265), (-26767,-51264))</a:Rect>
<a:ListOfPoints>((-26767,-51264),(-26767,-56265),(-40837,-56265))</a:ListOfPoints>
<a:CornerStyle>2</a:CornerStyle>
<a:ArrowStyle>7</a:ArrowStyle>
<a:LineColor>128</a:LineColor>
<a:ShadowColor>12632256</a:ShadowColor>
<a:FontList>DISPNAME 0 Arial,8,N</a:FontList>
<c:SourceSymbol>
<o:UseCaseSymbol Ref="o97"/>
</c:SourceSymbol>
<c:DestinationSymbol>
<o:UseCaseSymbol Ref="o94"/>
</c:DestinationSymbol>
<c:Object>
<o:Generalization Ref="o98"/>
</c:Object>
</o:GeneralizationSymbol>
<o:UseCaseAssociationSymbol Id="o99">
<a:CreationDate>1767375343</a:CreationDate>
<a:ModificationDate>1767532623</a:ModificationDate>
<a:Rect>((-36195,-2706), (-15854,31629))</a:Rect>
<a:ListOfPoints>((-36195,-2706),(-15854,-2706),(-15854,31629))</a:ListOfPoints>
<a:CornerStyle>2</a:CornerStyle>
<a:ArrowStyle>0</a:ArrowStyle>
<a:LineColor>128</a:LineColor>
<a:ShadowColor>12632256</a:ShadowColor>
<a:FontList>DISPNAME 0 Arial,8,N</a:FontList>
<c:SourceSymbol>
<o:ActorSymbol Ref="o100"/>
</c:SourceSymbol>
<c:DestinationSymbol>
<o:UseCaseSymbol Ref="o46"/>
</c:DestinationSymbol>
<c:Object>
<o:UseCaseAssociation Ref="o101"/>
</c:Object>
</o:UseCaseAssociationSymbol>
<o:UseCaseAssociationSymbol Id="o102">
<a:CreationDate>1767375345</a:CreationDate>
<a:ModificationDate>1767532735</a:ModificationDate>
<a:Rect>((-36525,-1716), (-5437,10832))</a:Rect>
<a:ListOfPoints>((-36525,-1716),(-5437,-1716),(-5437,10832))</a:ListOfPoints>
<a:CornerStyle>2</a:CornerStyle>
<a:ArrowStyle>0</a:ArrowStyle>
<a:LineColor>128</a:LineColor>
<a:ShadowColor>12632256</a:ShadowColor>
<a:FontList>DISPNAME 0 Arial,8,N</a:FontList>
<c:SourceSymbol>
<o:ActorSymbol Ref="o100"/>
</c:SourceSymbol>
<c:DestinationSymbol>
<o:UseCaseSymbol Ref="o31"/>
</c:DestinationSymbol>
<c:Object>
<o:UseCaseAssociation Ref="o103"/>
</c:Object>
</o:UseCaseAssociationSymbol>
<o:UseCaseAssociationSymbol Id="o104">
<a:CreationDate>1767375349</a:CreationDate>
<a:ModificationDate>1767532399</a:ModificationDate>
<a:Rect>((-35865,-22561), (-5459,-2320))</a:Rect>
<a:ListOfPoints>((-35865,-2320),(-5459,-2320),(-5459,-22561))</a:ListOfPoints>
<a:CornerStyle>2</a:CornerStyle>
<a:ArrowStyle>0</a:ArrowStyle>
<a:LineColor>128</a:LineColor>
<a:ShadowColor>12632256</a:ShadowColor>
<a:FontList>DISPNAME 0 Arial,8,N</a:FontList>
<c:SourceSymbol>
<o:ActorSymbol Ref="o100"/>
</c:SourceSymbol>
<c:DestinationSymbol>
<o:UseCaseSymbol Ref="o56"/>
</c:DestinationSymbol>
<c:Object>
<o:UseCaseAssociation Ref="o105"/>
</c:Object>
</o:UseCaseAssociationSymbol>
<o:UseCaseAssociationSymbol Id="o106">
<a:CreationDate>1767375353</a:CreationDate>
<a:ModificationDate>1767532668</a:ModificationDate>
<a:Rect>((-38460,-51344), (-2917,-4536))</a:Rect>
<a:ListOfPoints>((-38460,-4536),(-2917,-4536),(-2917,-51344))</a:ListOfPoints>
<a:CornerStyle>2</a:CornerStyle>
<a:ArrowStyle>0</a:ArrowStyle>
<a:LineColor>128</a:LineColor>
<a:ShadowColor>12632256</a:ShadowColor>
<a:FontList>DISPNAME 0 Arial,8,N</a:FontList>
<c:SourceSymbol>
<o:ActorSymbol Ref="o100"/>
</c:SourceSymbol>
<c:DestinationSymbol>
<o:UseCaseSymbol Ref="o84"/>
</c:DestinationSymbol>
<c:Object>
<o:UseCaseAssociation Ref="o107"/>
</c:Object>
</o:UseCaseAssociationSymbol>
<o:UseCaseAssociationSymbol Id="o108">
<a:CreationDate>1767375365</a:CreationDate>
<a:ModificationDate>1767532692</a:ModificationDate>
<a:Rect>((-49169,-56245), (-36195,-4123))</a:Rect>
<a:ListOfPoints>((-36195,-4123),(-49169,-4123),(-49169,-56245))</a:ListOfPoints>
<a:CornerStyle>2</a:CornerStyle>
<a:ArrowStyle>0</a:ArrowStyle>
<a:LineColor>128</a:LineColor>
<a:ShadowColor>12632256</a:ShadowColor>
<a:FontList>DISPNAME 0 Arial,8,N</a:FontList>
<c:SourceSymbol>
<o:ActorSymbol Ref="o100"/>
</c:SourceSymbol>
<c:DestinationSymbol>
<o:UseCaseSymbol Ref="o94"/>
</c:DestinationSymbol>
<c:Object>
<o:UseCaseAssociation Ref="o109"/>
</c:Object>
</o:UseCaseAssociationSymbol>
<o:TextSymbol Id="o110">
<a:Text>Système BabyCare</a:Text>
<a:CreationDate>1767369220</a:CreationDate>
<a:ModificationDate>1767375852</a:ModificationDate>
<a:Rect>((6,44518), (14706,40576))</a:Rect>
<a:TextStyle>4130</a:TextStyle>
<a:AutoAdjustToText>0</a:AutoAdjustToText>
<a:LineColor>0</a:LineColor>
<a:DashStyle>7</a:DashStyle>
<a:FillColor>0</a:FillColor>
<a:ShadowColor>12632256</a:ShadowColor>
<a:FontName>Arial,8,N</a:FontName>
<a:ManuallyResized>1</a:ManuallyResized>
</o:TextSymbol>
<o:ActorSymbol Id="o100">
<a:CreationDate>1767369332</a:CreationDate>
<a:ModificationDate>1767532183</a:ModificationDate>
<a:IconMode>-1</a:IconMode>
<a:Rect>((-38504,-4552), (-33705,-953))</a:Rect>
<a:LineColor>128</a:LineColor>
<a:LineWidth>1</a:LineWidth>
<a:FillColor>4210816</a:FillColor>
<a:ShadowColor>12632256</a:ShadowColor>
<a:FontList>STRN 0 Arial,8,N
DISPNAME 0 Arial,8,N</a:FontList>
<a:BrushStyle>6</a:BrushStyle>
<a:GradientFillMode>65</a:GradientFillMode>
<a:GradientEndColor>16777215</a:GradientEndColor>
<a:KeepAspect>1</a:KeepAspect>
<a:KeepCenter>1</a:KeepCenter>
<c:Object>
<o:Actor Ref="o111"/>
</c:Object>
</o:ActorSymbol>
<o:UseCaseSymbol Id="o46">
<a:CreationDate>1767369664</a:CreationDate>
<a:ModificationDate>1767532605</a:ModificationDate>
<a:Rect>((-16020,29768), (-6420,35167))</a:Rect>
<a:AutoAdjustToText>0</a:AutoAdjustToText>
<a:LineColor>128</a:LineColor>
<a:LineWidth>1</a:LineWidth>
<a:FillColor>10473471</a:FillColor>
<a:ShadowColor>12632256</a:ShadowColor>
<a:FontList>STRN 0 Arial,8,N
DISPNAME 0 Arial,8,N
LABL 0 Arial,8,N</a:FontList>
<a:BrushStyle>6</a:BrushStyle>
<a:GradientFillMode>16</a:GradientFillMode>
<a:GradientEndColor>16777215</a:GradientEndColor>
<a:ManuallyResized>1</a:ManuallyResized>
<c:Object>
<o:UseCase Ref="o112"/>
</c:Object>
</o:UseCaseSymbol>
<o:UseCaseSymbol Id="o49">
<a:CreationDate>1767369664</a:CreationDate>
<a:ModificationDate>1767532607</a:ModificationDate>
<a:Rect>((-7026,24990), (2622,28965))</a:Rect>
<a:AutoAdjustToText>0</a:AutoAdjustToText>
<a:LineColor>128</a:LineColor>
<a:LineWidth>1</a:LineWidth>
<a:FillColor>10473471</a:FillColor>
<a:ShadowColor>12632256</a:ShadowColor>
<a:FontList>STRN 0 Arial,8,N
DISPNAME 0 Arial,8,N
LABL 0 Arial,8,N</a:FontList>
<a:BrushStyle>6</a:BrushStyle>
<a:GradientFillMode>16</a:GradientFillMode>
<a:GradientEndColor>16777215</a:GradientEndColor>
<a:ManuallyResized>1</a:ManuallyResized>
<c:Object>
<o:UseCase Ref="o113"/>
</c:Object>
</o:UseCaseSymbol>
<o:UseCaseSymbol Id="o45">
<a:CreationDate>1767369755</a:CreationDate>
<a:ModificationDate>1767532611</a:ModificationDate>
<a:Rect>((7487,33375), (18661,37276))</a:Rect>
<a:AutoAdjustToText>0</a:AutoAdjustToText>
<a:LineColor>128</a:LineColor>
<a:LineWidth>1</a:LineWidth>
<a:FillColor>10473471</a:FillColor>
<a:ShadowColor>12632256</a:ShadowColor>
<a:FontList>STRN 0 Arial,8,N
DISPNAME 0 Arial,8,N
LABL 0 Arial,8,N</a:FontList>
<a:BrushStyle>6</a:BrushStyle>
<a:GradientFillMode>16</a:GradientFillMode>
<a:GradientEndColor>16777215</a:GradientEndColor>
<a:ManuallyResized>1</a:ManuallyResized>
<c:Object>
<o:UseCase Ref="o114"/>
</c:Object>
</o:UseCaseSymbol>
<o:UseCaseSymbol Id="o52">
<a:CreationDate>1767369952</a:CreationDate>
<a:ModificationDate>1767532609</a:ModificationDate>
<a:Rect>((4110,25612), (14384,29811))</a:Rect>
<a:AutoAdjustToText>0</a:AutoAdjustToText>
<a:LineColor>128</a:LineColor>
<a:LineWidth>1</a:LineWidth>
<a:FillColor>10473471</a:FillColor>
<a:ShadowColor>12632256</a:ShadowColor>
<a:FontList>STRN 0 Arial,8,N
DISPNAME 0 Arial,8,N
LABL 0 Arial,8,N</a:FontList>
<a:BrushStyle>6</a:BrushStyle>
<a:GradientFillMode>16</a:GradientFillMode>
<a:GradientEndColor>16777215</a:GradientEndColor>
<a:ManuallyResized>1</a:ManuallyResized>
<c:Object>
<o:UseCase Ref="o115"/>
</c:Object>
</o:UseCaseSymbol>
<o:UseCaseSymbol Id="o31">
<a:CreationDate>1767370341</a:CreationDate>
<a:ModificationDate>1767532735</a:ModificationDate>
<a:Rect>((-8730,9113), (1844,14512))</a:Rect>
<a:AutoAdjustToText>0</a:AutoAdjustToText>
<a:LineColor>128</a:LineColor>
<a:LineWidth>1</a:LineWidth>
<a:FillColor>10473471</a:FillColor>
<a:ShadowColor>12632256</a:ShadowColor>
<a:FontList>STRN 0 Arial,8,N
DISPNAME 0 Arial,8,N
LABL 0 Arial,8,N</a:FontList>
<a:BrushStyle>6</a:BrushStyle>
<a:GradientFillMode>16</a:GradientFillMode>
<a:GradientEndColor>16777215</a:GradientEndColor>
<a:ManuallyResized>1</a:ManuallyResized>
<c:Object>
<o:UseCase Ref="o116"/>
</c:Object>
</o:UseCaseSymbol>
<o:UseCaseSymbol Id="o42">
<a:CreationDate>1767370342</a:CreationDate>
<a:ModificationDate>1767532723</a:ModificationDate>
<a:Rect>((8490,14175), (22012,18600))</a:Rect>
<a:AutoAdjustToText>0</a:AutoAdjustToText>
<a:LineColor>128</a:LineColor>
<a:LineWidth>1</a:LineWidth>
<a:FillColor>10473471</a:FillColor>
<a:ShadowColor>12632256</a:ShadowColor>
<a:FontList>STRN 0 Arial,8,N
DISPNAME 0 Arial,8,N
LABL 0 Arial,8,N</a:FontList>
<a:BrushStyle>6</a:BrushStyle>
<a:GradientFillMode>16</a:GradientFillMode>
<a:GradientEndColor>16777215</a:GradientEndColor>
<a:ManuallyResized>1</a:ManuallyResized>
<c:Object>
<o:UseCase Ref="o117"/>
</c:Object>
</o:UseCaseSymbol>
<o:UseCaseSymbol Id="o8">
<a:CreationDate>1767370344</a:CreationDate>
<a:ModificationDate>1767532722</a:ModificationDate>
<a:Rect>((21491,10650), (33863,14849))</a:Rect>
<a:AutoAdjustToText>0</a:AutoAdjustToText>
<a:LineColor>128</a:LineColor>
<a:LineWidth>1</a:LineWidth>
<a:FillColor>10473471</a:FillColor>
<a:ShadowColor>12632256</a:ShadowColor>
<a:FontList>STRN 0 Arial,8,N
DISPNAME 0 Arial,8,N
LABL 0 Arial,8,N</a:FontList>
<a:BrushStyle>6</a:BrushStyle>
<a:GradientFillMode>16</a:GradientFillMode>
<a:GradientEndColor>16777215</a:GradientEndColor>
<a:ManuallyResized>1</a:ManuallyResized>
<c:Object>
<o:UseCase Ref="o118"/>
</c:Object>
</o:UseCaseSymbol>
<o:UseCaseSymbol Id="o7">
<a:CreationDate>1767370345</a:CreationDate>
<a:ModificationDate>1767532720</a:ModificationDate>
<a:Rect>((20016,1875), (33612,5924))</a:Rect>
<a:AutoAdjustToText>0</a:AutoAdjustToText>
<a:LineColor>128</a:LineColor>
<a:LineWidth>1</a:LineWidth>
<a:FillColor>10473471</a:FillColor>
<a:ShadowColor>12632256</a:ShadowColor>
<a:FontList>STRN 0 Arial,8,N
DISPNAME 0 Arial,8,N
LABL 0 Arial,8,N</a:FontList>
<a:BrushStyle>6</a:BrushStyle>
<a:GradientFillMode>16</a:GradientFillMode>
<a:GradientEndColor>16777215</a:GradientEndColor>
<a:ManuallyResized>1</a:ManuallyResized>
<c:Object>
<o:UseCase Ref="o119"/>
</c:Object>
</o:UseCaseSymbol>
<o:UseCaseSymbol Id="o36">
<a:CreationDate>1767370463</a:CreationDate>
<a:ModificationDate>1767532725</a:ModificationDate>
<a:Rect>((13139,-2250), (23237,1425))</a:Rect>
<a:AutoAdjustToText>0</a:AutoAdjustToText>
<a:LineColor>128</a:LineColor>
<a:LineWidth>1</a:LineWidth>
<a:FillColor>10473471</a:FillColor>
<a:ShadowColor>12632256</a:ShadowColor>
<a:FontList>STRN 0 Arial,8,N
DISPNAME 0 Arial,8,N
LABL 0 Arial,8,N</a:FontList>
<a:BrushStyle>6</a:BrushStyle>
<a:GradientFillMode>16</a:GradientFillMode>
<a:GradientEndColor>16777215</a:GradientEndColor>
<a:ManuallyResized>1</a:ManuallyResized>
<c:Object>
<o:UseCase Ref="o120"/>
</c:Object>
</o:UseCaseSymbol>
<o:UseCaseSymbol Id="o39">
<a:CreationDate>1767370465</a:CreationDate>
<a:ModificationDate>1767532727</a:ModificationDate>
<a:Rect>((-3835,-825), (11261,3300))</a:Rect>
<a:AutoAdjustToText>0</a:AutoAdjustToText>
<a:LineColor>128</a:LineColor>
<a:LineWidth>1</a:LineWidth>
<a:FillColor>10473471</a:FillColor>
<a:ShadowColor>12632256</a:ShadowColor>
<a:FontList>STRN 0 Arial,8,N
DISPNAME 0 Arial,8,N
LABL 0 Arial,8,N</a:FontList>
<a:BrushStyle>6</a:BrushStyle>
<a:GradientFillMode>16</a:GradientFillMode>
<a:GradientEndColor>16777215</a:GradientEndColor>
<a:ManuallyResized>1</a:ManuallyResized>
<c:Object>
<o:UseCase Ref="o121"/>
</c:Object>
</o:UseCaseSymbol>
<o:UseCaseSymbol Id="o56">
<a:CreationDate>1767373440</a:CreationDate>
<a:ModificationDate>1767375813</a:ModificationDate>
<a:Rect>((-7435,-22844), (1362,-17969))</a:Rect>
<a:AutoAdjustToText>0</a:AutoAdjustToText>
<a:LineColor>128</a:LineColor>
<a:LineWidth>1</a:LineWidth>
<a:FillColor>10473471</a:FillColor>
<a:ShadowColor>12632256</a:ShadowColor>
<a:FontList>STRN 0 Arial,8,N
DISPNAME 0 Arial,8,N
LABL 0 Arial,8,N</a:FontList>
<a:BrushStyle>6</a:BrushStyle>
<a:GradientFillMode>16</a:GradientFillMode>
<a:GradientEndColor>16777215</a:GradientEndColor>
<a:ManuallyResized>1</a:ManuallyResized>
<c:Object>
<o:UseCase Ref="o122"/>
</c:Object>
</o:UseCaseSymbol>
<o:UseCaseSymbol Id="o65">
<a:CreationDate>1767373442</a:CreationDate>
<a:ModificationDate>1767373783</a:ModificationDate>
<a:Rect>((15338,-9149), (23288,-6525))</a:Rect>
<a:AutoAdjustToText>0</a:AutoAdjustToText>
<a:LineColor>128</a:LineColor>
<a:LineWidth>1</a:LineWidth>
<a:FillColor>10473471</a:FillColor>
<a:ShadowColor>12632256</a:ShadowColor>
<a:FontList>STRN 0 Arial,8,N
DISPNAME 0 Arial,8,N
LABL 0 Arial,8,N</a:FontList>
<a:BrushStyle>6</a:BrushStyle>
<a:GradientFillMode>16</a:GradientFillMode>
<a:GradientEndColor>16777215</a:GradientEndColor>
<a:ManuallyResized>1</a:ManuallyResized>
<c:Object>
<o:UseCase Ref="o123"/>
</c:Object>
</o:UseCaseSymbol>
<o:UseCaseSymbol Id="o55">
<a:CreationDate>1767373443</a:CreationDate>
<a:ModificationDate>1767375754</a:ModificationDate>
<a:Rect>((3046,-10860), (11296,-6361))</a:Rect>
<a:AutoAdjustToText>0</a:AutoAdjustToText>
<a:LineColor>128</a:LineColor>
<a:LineWidth>1</a:LineWidth>
<a:FillColor>10473471</a:FillColor>
<a:ShadowColor>12632256</a:ShadowColor>
<a:FontList>STRN 0 Arial,8,N
DISPNAME 0 Arial,8,N
LABL 0 Arial,8,N</a:FontList>
<a:BrushStyle>6</a:BrushStyle>
<a:GradientFillMode>16</a:GradientFillMode>
<a:GradientEndColor>16777215</a:GradientEndColor>
<a:ManuallyResized>1</a:ManuallyResized>
<c:Object>
<o:UseCase Ref="o124"/>
</c:Object>
</o:UseCaseSymbol>
<o:UseCaseSymbol Id="o59">
<a:CreationDate>1767373444</a:CreationDate>
<a:ModificationDate>1767375755</a:ModificationDate>
<a:Rect>((4411,-18593), (12209,-14768))</a:Rect>
<a:AutoAdjustToText>0</a:AutoAdjustToText>
<a:LineColor>128</a:LineColor>
<a:LineWidth>1</a:LineWidth>
<a:FillColor>10473471</a:FillColor>
<a:ShadowColor>12632256</a:ShadowColor>
<a:FontList>STRN 0 Arial,8,N
DISPNAME 0 Arial,8,N
LABL 0 Arial,8,N</a:FontList>
<a:BrushStyle>6</a:BrushStyle>
<a:GradientFillMode>16</a:GradientFillMode>
<a:GradientEndColor>16777215</a:GradientEndColor>
<a:ManuallyResized>1</a:ManuallyResized>
<c:Object>
<o:UseCase Ref="o125"/>
</c:Object>
</o:UseCaseSymbol>
<o:UseCaseSymbol Id="o62">
<a:CreationDate>1767373446</a:CreationDate>
<a:ModificationDate>1767375757</a:ModificationDate>
<a:Rect>((2666,-26340), (10264,-22065))</a:Rect>
<a:AutoAdjustToText>0</a:AutoAdjustToText>
<a:LineColor>128</a:LineColor>
<a:LineWidth>1</a:LineWidth>
<a:FillColor>10473471</a:FillColor>
<a:ShadowColor>12632256</a:ShadowColor>
<a:FontList>STRN 0 Arial,8,N
DISPNAME 0 Arial,8,N
LABL 0 Arial,8,N</a:FontList>
<a:BrushStyle>6</a:BrushStyle>
<a:GradientFillMode>16</a:GradientFillMode>
<a:GradientEndColor>16777215</a:GradientEndColor>
<a:ManuallyResized>1</a:ManuallyResized>
<c:Object>
<o:UseCase Ref="o126"/>
</c:Object>
</o:UseCaseSymbol>
<o:UseCaseSymbol Id="o68">
<a:CreationDate>1767373518</a:CreationDate>
<a:ModificationDate>1767373788</a:ModificationDate>
<a:Rect>((13915,-13127), (26811,-9900))</a:Rect>
<a:AutoAdjustToText>0</a:AutoAdjustToText>
<a:LineColor>128</a:LineColor>
<a:LineWidth>1</a:LineWidth>
<a:FillColor>10473471</a:FillColor>
<a:ShadowColor>12632256</a:ShadowColor>
<a:FontList>STRN 0 Arial,8,N
DISPNAME 0 Arial,8,N
LABL 0 Arial,8,N</a:FontList>
<a:BrushStyle>6</a:BrushStyle>
<a:GradientFillMode>16</a:GradientFillMode>
<a:GradientEndColor>16777215</a:GradientEndColor>
<a:ManuallyResized>1</a:ManuallyResized>
<c:Object>
<o:UseCase Ref="o127"/>
</c:Object>
</o:UseCaseSymbol>
<o:UseCaseSymbol Id="o71">
<a:CreationDate>1767373593</a:CreationDate>
<a:ModificationDate>1767373668</a:ModificationDate>
<a:Rect>((14888,-18452), (22088,-15975))</a:Rect>
<a:AutoAdjustToText>0</a:AutoAdjustToText>
<a:LineColor>128</a:LineColor>
<a:LineWidth>1</a:LineWidth>
<a:FillColor>10473471</a:FillColor>
<a:ShadowColor>12632256</a:ShadowColor>
<a:FontList>STRN 0 Arial,8,N
DISPNAME 0 Arial,8,N
LABL 0 Arial,8,N</a:FontList>
<a:BrushStyle>6</a:BrushStyle>
<a:GradientFillMode>16</a:GradientFillMode>
<a:GradientEndColor>16777215</a:GradientEndColor>
<a:ManuallyResized>1</a:ManuallyResized>
<c:Object>
<o:UseCase Ref="o128"/>
</c:Object>
</o:UseCaseSymbol>
<o:UseCaseSymbol Id="o74">
<a:CreationDate>1767373594</a:CreationDate>
<a:ModificationDate>1767373798</a:ModificationDate>
<a:Rect>((11516,-22500), (25911,-19575))</a:Rect>
<a:AutoAdjustToText>0</a:AutoAdjustToText>
<a:LineColor>128</a:LineColor>
<a:LineWidth>1</a:LineWidth>
<a:FillColor>10473471</a:FillColor>
<a:ShadowColor>12632256</a:ShadowColor>
<a:FontList>STRN 0 Arial,8,N
DISPNAME 0 Arial,8,N
LABL 0 Arial,8,N</a:FontList>
<a:BrushStyle>6</a:BrushStyle>
<a:GradientFillMode>16</a:GradientFillMode>
<a:GradientEndColor>16777215</a:GradientEndColor>
<a:ManuallyResized>1</a:ManuallyResized>
<c:Object>
<o:UseCase Ref="o129"/>
</c:Object>
</o:UseCaseSymbol>
<o:UseCaseSymbol Id="o77">
<a:CreationDate>1767373695</a:CreationDate>
<a:ModificationDate>1767373812</a:ModificationDate>
<a:Rect>((12342,-27975), (27936,-24000))</a:Rect>
<a:AutoAdjustToText>0</a:AutoAdjustToText>
<a:LineColor>128</a:LineColor>
<a:LineWidth>1</a:LineWidth>
<a:FillColor>10473471</a:FillColor>
<a:ShadowColor>12632256</a:ShadowColor>
<a:FontList>STRN 0 Arial,8,N
DISPNAME 0 Arial,8,N
LABL 0 Arial,8,N</a:FontList>
<a:BrushStyle>6</a:BrushStyle>
<a:GradientFillMode>16</a:GradientFillMode>
<a:GradientEndColor>16777215</a:GradientEndColor>
<a:ManuallyResized>1</a:ManuallyResized>
<c:Object>
<o:UseCase Ref="o130"/>
</c:Object>
</o:UseCaseSymbol>
<o:UseCaseSymbol Id="o80">
<a:CreationDate>1767373696</a:CreationDate>
<a:ModificationDate>1767373945</a:ModificationDate>
<a:Rect>((10163,-34200), (32687,-29774))</a:Rect>
<a:AutoAdjustToText>0</a:AutoAdjustToText>
<a:LineColor>128</a:LineColor>
<a:LineWidth>1</a:LineWidth>
<a:FillColor>10473471</a:FillColor>
<a:ShadowColor>12632256</a:ShadowColor>
<a:FontList>STRN 0 Arial,8,N
DISPNAME 0 Arial,8,N
LABL 0 Arial,8,N</a:FontList>
<a:BrushStyle>6</a:BrushStyle>
<a:GradientFillMode>16</a:GradientFillMode>
<a:GradientEndColor>16777215</a:GradientEndColor>
<a:ManuallyResized>1</a:ManuallyResized>
<c:Object>
<o:UseCase Ref="o131"/>
</c:Object>
</o:UseCaseSymbol>
<o:UseCaseSymbol Id="o84">
<a:CreationDate>1767374157</a:CreationDate>
<a:ModificationDate>1767532654</a:ModificationDate>
<a:Rect>((-3883,-54864), (15312,-49913))</a:Rect>
<a:AutoAdjustToText>0</a:AutoAdjustToText>
<a:LineColor>128</a:LineColor>
<a:LineWidth>1</a:LineWidth>
<a:FillColor>10473471</a:FillColor>
<a:ShadowColor>12632256</a:ShadowColor>
<a:FontList>STRN 0 Arial,8,N
DISPNAME 0 Arial,8,N
LABL 0 Arial,8,N</a:FontList>
<a:BrushStyle>6</a:BrushStyle>
<a:GradientFillMode>16</a:GradientFillMode>
<a:GradientEndColor>16777215</a:GradientEndColor>
<a:ManuallyResized>1</a:ManuallyResized>
<c:Object>
<o:UseCase Ref="o132"/>
</c:Object>
</o:UseCaseSymbol>
<o:UseCaseSymbol Id="o83">
<a:CreationDate>1767374168</a:CreationDate>
<a:ModificationDate>1767532677</a:ModificationDate>
<a:Rect>((21355,-62327), (35949,-57450))</a:Rect>
<a:AutoAdjustToText>0</a:AutoAdjustToText>
<a:LineColor>128</a:LineColor>
<a:LineWidth>1</a:LineWidth>
<a:FillColor>10473471</a:FillColor>
<a:ShadowColor>12632256</a:ShadowColor>
<a:FontList>STRN 0 Arial,8,N
DISPNAME 0 Arial,8,N
LABL 0 Arial,8,N</a:FontList>
<a:BrushStyle>6</a:BrushStyle>
<a:GradientFillMode>16</a:GradientFillMode>
<a:GradientEndColor>16777215</a:GradientEndColor>
<a:ManuallyResized>1</a:ManuallyResized>
<c:Object>
<o:UseCase Ref="o133"/>
</c:Object>
</o:UseCaseSymbol>
<o:UseCaseSymbol Id="o87">
<a:CreationDate>1767374169</a:CreationDate>
<a:ModificationDate>1767532674</a:ModificationDate>
<a:Rect>((24874,-50042), (39568,-45683))</a:Rect>
<a:AutoAdjustToText>0</a:AutoAdjustToText>
<a:LineColor>128</a:LineColor>
<a:LineWidth>1</a:LineWidth>
<a:FillColor>10473471</a:FillColor>
<a:ShadowColor>12632256</a:ShadowColor>
<a:FontList>STRN 0 Arial,8,N
DISPNAME 0 Arial,8,N
LABL 0 Arial,8,N</a:FontList>
<a:BrushStyle>6</a:BrushStyle>
<a:GradientFillMode>16</a:GradientFillMode>
<a:GradientEndColor>16777215</a:GradientEndColor>
<a:ManuallyResized>1</a:ManuallyResized>
<c:Object>
<o:UseCase Ref="o134"/>
</c:Object>
</o:UseCaseSymbol>
<o:UseCaseSymbol Id="o90">
<a:CreationDate>1767374171</a:CreationDate>
<a:ModificationDate>1767532675</a:ModificationDate>
<a:Rect>((24442,-56102), (39836,-51931))</a:Rect>
<a:AutoAdjustToText>0</a:AutoAdjustToText>
<a:LineColor>128</a:LineColor>
<a:LineWidth>1</a:LineWidth>
<a:FillColor>10473471</a:FillColor>
<a:ShadowColor>12632256</a:ShadowColor>
<a:FontList>STRN 0 Arial,8,N
DISPNAME 0 Arial,8,N
LABL 0 Arial,8,N</a:FontList>
<a:BrushStyle>6</a:BrushStyle>
<a:GradientFillMode>16</a:GradientFillMode>
<a:GradientEndColor>16777215</a:GradientEndColor>
<a:ManuallyResized>1</a:ManuallyResized>
<c:Object>
<o:UseCase Ref="o135"/>
</c:Object>
</o:UseCaseSymbol>
<o:UseCaseSymbol Id="o94">
<a:CreationDate>1767374605</a:CreationDate>
<a:ModificationDate>1767532692</a:ModificationDate>
<a:Rect>((-51644,-58094), (-39682,-52694))</a:Rect>
<a:AutoAdjustToText>0</a:AutoAdjustToText>
<a:LineColor>128</a:LineColor>
<a:LineWidth>1</a:LineWidth>
<a:FillColor>10473471</a:FillColor>
<a:ShadowColor>12632256</a:ShadowColor>
<a:FontList>STRN 0 Arial,8,N
DISPNAME 0 Arial,8,N
LABL 0 Arial,8,N</a:FontList>
<a:BrushStyle>6</a:BrushStyle>
<a:GradientFillMode>16</a:GradientFillMode>
<a:GradientEndColor>16777215</a:GradientEndColor>
<a:ManuallyResized>1</a:ManuallyResized>
<c:Object>
<o:UseCase Ref="o136"/>
</c:Object>
</o:UseCaseSymbol>
<o:UseCaseSymbol Id="o93">
<a:CreationDate>1767374606</a:CreationDate>
<a:ModificationDate>1767532697</a:ModificationDate>
<a:Rect>((-31543,-63330), (-13348,-58685))</a:Rect>
<a:AutoAdjustToText>0</a:AutoAdjustToText>
<a:LineColor>128</a:LineColor>
<a:LineWidth>1</a:LineWidth>
<a:FillColor>10473471</a:FillColor>
<a:ShadowColor>12632256</a:ShadowColor>
<a:FontList>STRN 0 Arial,8,N
DISPNAME 0 Arial,8,N
LABL 0 Arial,8,N</a:FontList>
<a:BrushStyle>6</a:BrushStyle>
<a:GradientFillMode>16</a:GradientFillMode>
<a:GradientEndColor>16777215</a:GradientEndColor>
<a:ManuallyResized>1</a:ManuallyResized>
<c:Object>
<o:UseCase Ref="o137"/>
</c:Object>
</o:UseCaseSymbol>
<o:UseCaseSymbol Id="o97">
<a:CreationDate>1767374607</a:CreationDate>
<a:ModificationDate>1767532694</a:ModificationDate>
<a:Rect>((-29655,-53925), (-12949,-49693))</a:Rect>
<a:AutoAdjustToText>0</a:AutoAdjustToText>
<a:LineColor>128</a:LineColor>
<a:LineWidth>1</a:LineWidth>
<a:FillColor>10473471</a:FillColor>
<a:ShadowColor>12632256</a:ShadowColor>
<a:FontList>STRN 0 Arial,8,N
DISPNAME 0 Arial,8,N
LABL 0 Arial,8,N</a:FontList>
<a:BrushStyle>6</a:BrushStyle>
<a:GradientFillMode>16</a:GradientFillMode>
<a:GradientEndColor>16777215</a:GradientEndColor>
<a:ManuallyResized>1</a:ManuallyResized>
<c:Object>
<o:UseCase Ref="o138"/>
</c:Object>
</o:UseCaseSymbol>
<o:UseCaseSymbol Id="o139">
<a:CreationDate>1767532797</a:CreationDate>
<a:ModificationDate>1767559077</a:ModificationDate>
<a:Rect>((-40526,-16547), (-27030,-13022))</a:Rect>
<a:AutoAdjustToText>0</a:AutoAdjustToText>
<a:LineColor>128</a:LineColor>
<a:LineWidth>1</a:LineWidth>
<a:FillColor>10473471</a:FillColor>
<a:ShadowColor>12632256</a:ShadowColor>
<a:FontList>STRN 0 Arial,8,N
DISPNAME 0 Arial,8,N
LABL 0 Arial,8,N</a:FontList>
<a:BrushStyle>6</a:BrushStyle>
<a:GradientFillMode>16</a:GradientFillMode>
<a:GradientEndColor>16777215</a:GradientEndColor>
<a:ManuallyResized>1</a:ManuallyResized>
<c:Object>
<o:UseCase Ref="o140"/>
</c:Object>
</o:UseCaseSymbol>
<o:UseCaseSymbol Id="o11">
<a:CreationDate>1767532812</a:CreationDate>
<a:ModificationDate>1767559078</a:ModificationDate>
<a:Rect>((-38581,-22881), (-28084,-19206))</a:Rect>
<a:AutoAdjustToText>0</a:AutoAdjustToText>
<a:LineColor>128</a:LineColor>
<a:LineWidth>1</a:LineWidth>
<a:FillColor>10473471</a:FillColor>
<a:ShadowColor>12632256</a:ShadowColor>
<a:FontList>STRN 0 Arial,8,N
DISPNAME 0 Arial,8,N
LABL 0 Arial,8,N</a:FontList>
<a:BrushStyle>6</a:BrushStyle>
<a:GradientFillMode>16</a:GradientFillMode>
<a:GradientEndColor>16777215</a:GradientEndColor>
<a:ManuallyResized>1</a:ManuallyResized>
<c:Object>
<o:UseCase Ref="o141"/>
</c:Object>
</o:UseCaseSymbol>
<o:UseCaseSymbol Id="o12">
<a:CreationDate>1767532812</a:CreationDate>
<a:ModificationDate>1767559081</a:ModificationDate>
<a:Rect>((-37753,-29075), (-28756,-25400))</a:Rect>
<a:AutoAdjustToText>0</a:AutoAdjustToText>
<a:LineColor>128</a:LineColor>
<a:LineWidth>1</a:LineWidth>
<a:FillColor>10473471</a:FillColor>
<a:ShadowColor>12632256</a:ShadowColor>
<a:FontList>STRN 0 Arial,8,N
DISPNAME 0 Arial,8,N
LABL 0 Arial,8,N</a:FontList>
<a:BrushStyle>6</a:BrushStyle>
<a:GradientFillMode>16</a:GradientFillMode>
<a:GradientEndColor>16777215</a:GradientEndColor>
<a:ManuallyResized>1</a:ManuallyResized>
<c:Object>
<o:UseCase Ref="o142"/>
</c:Object>
</o:UseCaseSymbol>
</c:Symbols>
</o:UseCaseDiagram>
</c:UseCaseDiagrams>
<c:Generalizations>
<o:Generalization Id="o32">
<a:ObjectID>95C4E15D-9EAC-4FD0-B2C8-B8707FF0809C</a:ObjectID>
<a:Name>Generalisation_4</a:Name>
<a:Code>Generalisation_4</a:Code>
<a:CreationDate>1767370603</a:CreationDate>
<a:Creator>houda</a:Creator>
<a:ModificationDate>1767370603</a:ModificationDate>
<a:Modifier>houda</a:Modifier>
<c:Object1>
<o:UseCase Ref="o116"/>
</c:Object1>
<c:Object2>
<o:UseCase Ref="o118"/>
</c:Object2>
</o:Generalization>
<o:Generalization Id="o34">
<a:ObjectID>3FB13CD1-84A0-40F0-BDF4-A0DBD13C34A5</a:ObjectID>
<a:Name>Generalisation_5</a:Name>
<a:Code>Generalisation_5</a:Code>
<a:CreationDate>1767370605</a:CreationDate>
<a:Creator>houda</a:Creator>
<a:ModificationDate>1767370605</a:ModificationDate>
<a:Modifier>houda</a:Modifier>
<c:Object1>
<o:UseCase Ref="o116"/>
</c:Object1>
<c:Object2>
<o:UseCase Ref="o119"/>
</c:Object2>
</o:Generalization>
<o:Generalization Id="o37">
<a:ObjectID>B2A38E0A-1FDB-40AF-971E-CA6B1A30C64B</a:ObjectID>
<a:Name>Generalisation_6</a:Name>
<a:Code>Generalisation_6</a:Code>
<a:CreationDate>1767370607</a:CreationDate>
<a:Creator>houda</a:Creator>
<a:ModificationDate>1767370607</a:ModificationDate>
<a:Modifier>houda</a:Modifier>
<c:Object1>
<o:UseCase Ref="o116"/>
</c:Object1>
<c:Object2>
<o:UseCase Ref="o120"/>
</c:Object2>
</o:Generalization>
<o:Generalization Id="o40">
<a:ObjectID>2FEF8AF9-75EF-4E71-99DA-5258C4B36B82</a:ObjectID>
<a:Name>Generalisation_7</a:Name>
<a:Code>Generalisation_7</a:Code>
<a:CreationDate>1767370610</a:CreationDate>
<a:Creator>houda</a:Creator>
<a:ModificationDate>1767370610</a:ModificationDate>
<a:Modifier>houda</a:Modifier>
<c:Object1>
<o:UseCase Ref="o116"/>
</c:Object1>
<c:Object2>
<o:UseCase Ref="o121"/>
</c:Object2>
</o:Generalization>
<o:Generalization Id="o43">
<a:ObjectID>F8B2A499-2F7F-4A1B-A203-2D9D537D0EE2</a:ObjectID>
<a:Name>Generalisation_8</a:Name>
<a:Code>Generalisation_8</a:Code>
<a:CreationDate>1767370664</a:CreationDate>
<a:Creator>houda</a:Creator>
<a:ModificationDate>1767370664</a:ModificationDate>
<a:Modifier>houda</a:Modifier>
<c:Object1>
<o:UseCase Ref="o116"/>
</c:Object1>
<c:Object2>
<o:UseCase Ref="o117"/>
</c:Object2>
</o:Generalization>
<o:Generalization Id="o47">
<a:ObjectID>50B6EAC9-445F-4E7E-82AA-BFB5F9DA8CE8</a:ObjectID>
<a:Name>Generalisation_9</a:Name>
<a:Code>Generalisation_9</a:Code>
<a:CreationDate>1767373301</a:CreationDate>
<a:Creator>houda</a:Creator>
<a:ModificationDate>1767373301</a:ModificationDate>
<a:Modifier>houda</a:Modifier>
<c:Object1>
<o:UseCase Ref="o112"/>
</c:Object1>
<c:Object2>
<o:UseCase Ref="o114"/>
</c:Object2>
</o:Generalization>
<o:Generalization Id="o50">
<a:ObjectID>A57E4E31-3278-4D63-A8F7-4A260CB2F256</a:ObjectID>
<a:Name>Generalisation_10</a:Name>
<a:Code>Generalisation_10</a:Code>
<a:CreationDate>1767373305</a:CreationDate>
<a:Creator>houda</a:Creator>
<a:ModificationDate>1767373305</a:ModificationDate>
<a:Modifier>houda</a:Modifier>
<c:Object1>
<o:UseCase Ref="o112"/>
</c:Object1>
<c:Object2>
<o:UseCase Ref="o113"/>
</c:Object2>
</o:Generalization>
<o:Generalization Id="o53">
<a:ObjectID>64C91698-3F9D-4CC3-8B88-55400A67EB9B</a:ObjectID>
<a:Name>Generalisation_11</a:Name>
<a:Code>Generalisation_11</a:Code>
<a:CreationDate>1767373307</a:CreationDate>
<a:Creator>houda</a:Creator>
<a:ModificationDate>1767373307</a:ModificationDate>
<a:Modifier>houda</a:Modifier>
<c:Object1>
<o:UseCase Ref="o112"/>
</c:Object1>
<c:Object2>
<o:UseCase Ref="o115"/>
</c:Object2>
</o:Generalization>
<o:Generalization Id="o57">
<a:ObjectID>DAA9EF53-852B-4B25-94B6-C1C8D5B4F525</a:ObjectID>
<a:Name>Generalisation_12</a:Name>
<a:Code>Generalisation_12</a:Code>
<a:CreationDate>1767373839</a:CreationDate>
<a:Creator>houda</a:Creator>
<a:ModificationDate>1767373839</a:ModificationDate>
<a:Modifier>houda</a:Modifier>
<c:Object1>
<o:UseCase Ref="o122"/>
</c:Object1>
<c:Object2>
<o:UseCase Ref="o124"/>
</c:Object2>
</o:Generalization>
<o:Generalization Id="o60">
<a:ObjectID>394418D2-3D80-4635-B608-FFA124CCEEDA</a:ObjectID>
<a:Name>Generalisation_13</a:Name>
<a:Code>Generalisation_13</a:Code>
<a:CreationDate>1767373841</a:CreationDate>
<a:Creator>houda</a:Creator>
<a:ModificationDate>1767373841</a:ModificationDate>
<a:Modifier>houda</a:Modifier>
<c:Object1>
<o:UseCase Ref="o122"/>
</c:Object1>
<c:Object2>
<o:UseCase Ref="o125"/>
</c:Object2>
</o:Generalization>
<o:Generalization Id="o63">
<a:ObjectID>1756F4A7-C5DB-43E9-8225-9B952ABF1767</a:ObjectID>
<a:Name>Generalisation_14</a:Name>
<a:Code>Generalisation_14</a:Code>
<a:CreationDate>1767373848</a:CreationDate>
<a:Creator>houda</a:Creator>
<a:ModificationDate>1767373848</a:ModificationDate>
<a:Modifier>houda</a:Modifier>
<c:Object1>
<o:UseCase Ref="o122"/>
</c:Object1>
<c:Object2>
<o:UseCase Ref="o126"/>
</c:Object2>
</o:Generalization>
<o:Generalization Id="o66">
<a:ObjectID>D7E00981-32FB-4975-B83B-CE041E499E5D</a:ObjectID>
<a:Name>Generalisation_15</a:Name>
<a:Code>Generalisation_15</a:Code>
<a:CreationDate>1767373887</a:CreationDate>
<a:Creator>houda</a:Creator>
<a:ModificationDate>1767373887</a:ModificationDate>
<a:Modifier>houda</a:Modifier>
<c:Object1>
<o:UseCase Ref="o124"/>
</c:Object1>
<c:Object2>
<o:UseCase Ref="o123"/>
</c:Object2>
</o:Generalization>
<o:Generalization Id="o69">
<a:ObjectID>559A1607-206A-4E93-A99F-862E80DE1052</a:ObjectID>
<a:Name>Generalisation_16</a:Name>
<a:Code>Generalisation_16</a:Code>
<a:CreationDate>1767373899</a:CreationDate>
<a:Creator>houda</a:Creator>
<a:ModificationDate>1767373899</a:ModificationDate>
<a:Modifier>houda</a:Modifier>
<c:Object1>
<o:UseCase Ref="o124"/>
</c:Object1>
<c:Object2>
<o:UseCase Ref="o127"/>
</c:Object2>
</o:Generalization>
<o:Generalization Id="o72">
<a:ObjectID>C787A64E-FEE6-44D2-891B-A1C23B6FF3B6</a:ObjectID>
<a:Name>Generalisation_17</a:Name>
<a:Code>Generalisation_17</a:Code>
<a:CreationDate>1767373903</a:CreationDate>
<a:Creator>houda</a:Creator>
<a:ModificationDate>1767373903</a:ModificationDate>
<a:Modifier>houda</a:Modifier>
<c:Object1>
<o:UseCase Ref="o125"/>
</c:Object1>
<c:Object2>
<o:UseCase Ref="o128"/>
</c:Object2>
</o:Generalization>
<o:Generalization Id="o75">
<a:ObjectID>3D903309-0D15-470A-BDE0-08E95F4C84D4</a:ObjectID>
<a:Name>Generalisation_18</a:Name>
<a:Code>Generalisation_18</a:Code>
<a:CreationDate>1767373904</a:CreationDate>
<a:Creator>houda</a:Creator>
<a:ModificationDate>1767373904</a:ModificationDate>
<a:Modifier>houda</a:Modifier>
<c:Object1>
<o:UseCase Ref="o125"/>
</c:Object1>
<c:Object2>
<o:UseCase Ref="o129"/>
</c:Object2>
</o:Generalization>
<o:Generalization Id="o78">
<a:ObjectID>A18FB7BF-2F05-40A3-97D6-E7426094F73D</a:ObjectID>
<a:Name>Generalisation_19</a:Name>
<a:Code>Generalisation_19</a:Code>
<a:CreationDate>1767373906</a:CreationDate>
<a:Creator>houda</a:Creator>
<a:ModificationDate>1767373906</a:ModificationDate>
<a:Modifier>houda</a:Modifier>
<c:Object1>
<o:UseCase Ref="o126"/>
</c:Object1>
<c:Object2>
<o:UseCase Ref="o130"/>
</c:Object2>
</o:Generalization>
<o:Generalization Id="o81">
<a:ObjectID>C19833AD-1AC1-4A71-A213-88BB4E8E889C</a:ObjectID>
<a:Name>Generalisation_20</a:Name>
<a:Code>Generalisation_20</a:Code>
<a:CreationDate>1767373910</a:CreationDate>
<a:Creator>houda</a:Creator>
<a:ModificationDate>1767373910</a:ModificationDate>
<a:Modifier>houda</a:Modifier>
<c:Object1>
<o:UseCase Ref="o126"/>
</c:Object1>
<c:Object2>
<o:UseCase Ref="o131"/>
</c:Object2>
</o:Generalization>
<o:Generalization Id="o85">
<a:ObjectID>497A951C-8947-4494-BCCB-0BBEFAF95F7B</a:ObjectID>
<a:Name>Generalisation_21</a:Name>
<a:Code>Generalisation_21</a:Code>
<a:CreationDate>1767374529</a:CreationDate>
<a:Creator>houda</a:Creator>
<a:ModificationDate>1767374529</a:ModificationDate>
<a:Modifier>houda</a:Modifier>
<c:Object1>
<o:UseCase Ref="o132"/>
</c:Object1>
<c:Object2>
<o:UseCase Ref="o133"/>
</c:Object2>
</o:Generalization>
<o:Generalization Id="o88">
<a:ObjectID>724A7A0A-2FC7-4403-8B14-510FB2BD99B1</a:ObjectID>
<a:Name>Generalisation_22</a:Name>
<a:Code>Generalisation_22</a:Code>
<a:CreationDate>1767374535</a:CreationDate>
<a:Creator>houda</a:Creator>
<a:ModificationDate>1767374535</a:ModificationDate>
<a:Modifier>houda</a:Modifier>
<c:Object1>
<o:UseCase Ref="o132"/>
</c:Object1>
<c:Object2>
<o:UseCase Ref="o134"/>
</c:Object2>
</o:Generalization>
<o:Generalization Id="o91">
<a:ObjectID>8F108614-94BF-4EF2-AD3D-3051B636898D</a:ObjectID>
<a:Name>Generalisation_23</a:Name>
<a:Code>Generalisation_23</a:Code>
<a:CreationDate>1767374539</a:CreationDate>
<a:Creator>houda</a:Creator>
<a:ModificationDate>1767374539</a:ModificationDate>
<a:Modifier>houda</a:Modifier>
<c:Object1>
<o:UseCase Ref="o132"/>
</c:Object1>
<c:Object2>
<o:UseCase Ref="o135"/>
</c:Object2>
</o:Generalization>
<o:Generalization Id="o95">
<a:ObjectID>B69C2BA4-C141-4F52-8BBA-93EA552C5552</a:ObjectID>
<a:Name>Generalisation_24</a:Name>
<a:Code>Generalisation_24</a:Code>
<a:CreationDate>1767374722</a:CreationDate>
<a:Creator>houda</a:Creator>
<a:ModificationDate>1767374722</a:ModificationDate>
<a:Modifier>houda</a:Modifier>
<c:Object1>
<o:UseCase Ref="o136"/>
</c:Object1>
<c:Object2>
<o:UseCase Ref="o137"/>
</c:Object2>
</o:Generalization>
<o:Generalization Id="o98">
<a:ObjectID>2370A75D-439C-435F-9C7D-7259BCBA4292</a:ObjectID>
<a:Name>Generalisation_25</a:Name>
<a:Code>Generalisation_25</a:Code>
<a:CreationDate>1767374725</a:CreationDate>
<a:Creator>houda</a:Creator>
<a:ModificationDate>1767374725</a:ModificationDate>
<a:Modifier>houda</a:Modifier>
<c:Object1>
<o:UseCase Ref="o136"/>
</c:Object1>
<c:Object2>
<o:UseCase Ref="o138"/>
</c:Object2>
</o:Generalization>
</c:Generalizations>
<c:Dependencies>
<o:Dependency Id="o19">
<a:ObjectID>1598577F-6AE6-4097-81E4-D8EB71BFC08C</a:ObjectID>
<a:Name>Dependance_1</a:Name>
<a:Code>Dependance_1</a:Code>
<a:CreationDate>1767532491</a:CreationDate>
<a:Creator>houda</a:Creator>
<a:ModificationDate>1767532491</a:ModificationDate>
<a:Modifier>houda</a:Modifier>
<c:Object1>
<o:UseCase Ref="o118"/>
</c:Object1>
<c:Object2>
<o:UseCase Ref="o119"/>
</c:Object2>
</o:Dependency>
<o:Dependency Id="o21">
<a:ObjectID>89711146-5FA1-4A67-ADC4-E8EB59C99D8F</a:ObjectID>
<a:Name>Dependance_2</a:Name>
<a:Code>Dependance_2</a:Code>
<a:CreationDate>1767532495</a:CreationDate>
<a:Creator>houda</a:Creator>
<a:ModificationDate>1767532495</a:ModificationDate>
<a:Modifier>houda</a:Modifier>
<c:Object1>
<o:UseCase Ref="o119"/>
</c:Object1>
<c:Object2>
<o:UseCase Ref="o118"/>
</c:Object2>
</o:Dependency>
<o:Dependency Id="o9">
<a:ObjectID>19362E79-A6DA-4568-AA98-BE7F1B7F325E</a:ObjectID>
<a:Name>Dependance_4</a:Name>
<a:Code>Dependance_4</a:Code>
<a:CreationDate>1767558918</a:CreationDate>
<a:Creator>houda</a:Creator>
<a:ModificationDate>1767558918</a:ModificationDate>
<a:Modifier>houda</a:Modifier>
<c:Object1>
<o:UseCase Ref="o118"/>
</c:Object1>
<c:Object2>
<o:UseCase Ref="o119"/>
</c:Object2>
</o:Dependency>
<o:Dependency Id="o13">
<a:ObjectID>63365A86-B85D-4FC2-BB16-25176B37E29A</a:ObjectID>
<a:Name>Dependance_5</a:Name>
<a:Code>Dependance_5</a:Code>
<a:CreationDate>1767559042</a:CreationDate>
<a:Creator>houda</a:Creator>
<a:ModificationDate>1767559042</a:ModificationDate>
<a:Modifier>houda</a:Modifier>
<c:Object1>
<o:UseCase Ref="o142"/>
</c:Object1>
<c:Object2>
<o:UseCase Ref="o141"/>
</c:Object2>
</o:Dependency>
</c:Dependencies>
<c:Actors>
<o:Actor Id="o111">
<a:ObjectID>1F3591BA-DCF5-46E1-9877-353C90340CBD</a:ObjectID>
<a:Name>Utilisateur</a:Name>
<a:Code>Utilisateur</a:Code>
<a:CreationDate>1767369332</a:CreationDate>
<a:Creator>houda</a:Creator>
<a:ModificationDate>1767369413</a:ModificationDate>
<a:Modifier>houda</a:Modifier>
</o:Actor>
</c:Actors>
<c:UseCases>
<o:UseCase Id="o112">
<a:ObjectID>04F8160F-C7A4-4B3E-946A-1B1DEBF43779</a:ObjectID>
<a:Name>Gerer profil</a:Name>
<a:Code>Gerer_profil</a:Code>
<a:CreationDate>1767369664</a:CreationDate>
<a:Creator>houda</a:Creator>
<a:ModificationDate>1767369683</a:ModificationDate>
<a:Modifier>houda</a:Modifier>
</o:UseCase>
<o:UseCase Id="o113">
<a:ObjectID>7AA35A00-AD80-4A7B-9F71-076D87802DB6</a:ObjectID>
<a:Name>Consulter profil</a:Name>
<a:Code>Consulter_profil</a:Code>
<a:CreationDate>1767369664</a:CreationDate>
<a:Creator>houda</a:Creator>
<a:ModificationDate>1767369929</a:ModificationDate>
<a:Modifier>houda</a:Modifier>
</o:UseCase>
<o:UseCase Id="o114">
<a:ObjectID>2003DF75-C53C-4978-BFA4-C3134873617D</a:ObjectID>
<a:Name>Crèer profil bébé</a:Name>
<a:Code>Creer_profil_bebe</a:Code>
<a:CreationDate>1767369755</a:CreationDate>
<a:Creator>houda</a:Creator>
<a:ModificationDate>1767369933</a:ModificationDate>
<a:Modifier>houda</a:Modifier>
</o:UseCase>
<o:UseCase Id="o115">
<a:ObjectID>51B53E75-855F-4F8D-A902-E29320AADB4E</a:ObjectID>
<a:Name>Modifier profil</a:Name>
<a:Code>Modifier_profil</a:Code>
<a:CreationDate>1767369952</a:CreationDate>
<a:Creator>houda</a:Creator>
<a:ModificationDate>1767369969</a:ModificationDate>
<a:Modifier>houda</a:Modifier>
</o:UseCase>
<o:UseCase Id="o116">
<a:ObjectID>62EEE7BC-16CE-4298-8715-69B23D243773</a:ObjectID>
<a:Name>Suivre sante</a:Name>
<a:Code>Suivre_sante</a:Code>
<a:CreationDate>1767370341</a:CreationDate>
<a:Creator>houda</a:Creator>
<a:ModificationDate>1767370369</a:ModificationDate>
<a:Modifier>houda</a:Modifier>
</o:UseCase>
<o:UseCase Id="o117">
<a:ObjectID>73624DC6-5776-4483-A7F6-78503DF864DA</a:ObjectID>
<a:Name>Enregistrer poids et taille</a:Name>
<a:Code>Enregistrer_poids_et_taille</a:Code>
<a:CreationDate>1767370342</a:CreationDate>
<a:Creator>houda</a:Creator>
<a:ModificationDate>1767370386</a:ModificationDate>
<a:Modifier>houda</a:Modifier>
</o:UseCase>
<o:UseCase Id="o118">
<a:ObjectID>AA4A8087-CF9C-4728-AFE9-E25E2B819CEE</a:ObjectID>
<a:Name>Ajouter une vaccination</a:Name>
<a:Code>Ajouter_une_vaccination</a:Code>
<a:CreationDate>1767370344</a:CreationDate>
<a:Creator>houda</a:Creator>
<a:ModificationDate>1767370412</a:ModificationDate>
<a:Modifier>houda</a:Modifier>
</o:UseCase>
<o:UseCase Id="o119">
<a:ObjectID>2C69E00A-2D6B-42EC-98B0-411141FC4EB4</a:ObjectID>
<a:Name>Suivre calendrier de vaccin</a:Name>
<a:Code>Suivre_calendrier_de_vaccin</a:Code>
<a:CreationDate>1767370345</a:CreationDate>
<a:Creator>houda</a:Creator>
<a:ModificationDate>1767370433</a:ModificationDate>
<a:Modifier>houda</a:Modifier>
</o:UseCase>
<o:UseCase Id="o120">
<a:ObjectID>AA4191B0-5F6B-4BE9-9D42-F32442AFFAB7</a:ObjectID>
<a:Name>Ajouter rendez-vous</a:Name>
<a:Code>Ajouter_rendez_vous</a:Code>
<a:CreationDate>1767370463</a:CreationDate>
<a:Creator>houda</a:Creator>
<a:ModificationDate>1767370502</a:ModificationDate>
<a:Modifier>houda</a:Modifier>
</o:UseCase>
<o:UseCase Id="o121">
<a:ObjectID>6F396B20-7180-4902-9BF7-23368B4782B5</a:ObjectID>
<a:Name>Consulter l&#39;historique medicals</a:Name>
<a:Code>Consulter_l_historique_medicals</a:Code>
<a:CreationDate>1767370465</a:CreationDate>
<a:Creator>houda</a:Creator>
<a:ModificationDate>1767370520</a:ModificationDate>
<a:Modifier>houda</a:Modifier>
</o:UseCase>
<o:UseCase Id="o122">
<a:ObjectID>CC8D237B-33E2-4429-87A7-F83ED50896C8</a:ObjectID>
<a:Name>Suivre Quotidien</a:Name>
<a:Code>Suivre_Quotidien</a:Code>
<a:CreationDate>1767373440</a:CreationDate>
<a:Creator>houda</a:Creator>
<a:ModificationDate>1767373459</a:ModificationDate>
<a:Modifier>houda</a:Modifier>
</o:UseCase>
<o:UseCase Id="o123">
<a:ObjectID>55FA934A-FE25-4EE8-A2DD-B30B8D01A24D</a:ObjectID>
<a:Name>Ajouter repas</a:Name>
<a:Code>Ajouter_repas</a:Code>
<a:CreationDate>1767373442</a:CreationDate>
<a:Creator>houda</a:Creator>
<a:ModificationDate>1767373471</a:ModificationDate>
<a:Modifier>houda</a:Modifier>
</o:UseCase>
<o:UseCase Id="o124">
<a:ObjectID>E7B2348B-8A3C-4F78-8996-F692FA4D190D</a:ObjectID>
<a:Name>suivre repas</a:Name>
<a:Code>suivre_repas</a:Code>
<a:CreationDate>1767373443</a:CreationDate>
<a:Creator>houda</a:Creator>
<a:ModificationDate>1767373484</a:ModificationDate>
<a:Modifier>houda</a:Modifier>
</o:UseCase>
<o:UseCase Id="o125">
<a:ObjectID>29362AB7-5894-4F91-92B5-4EDC9338437C</a:ObjectID>
<a:Name>suivre sommeil</a:Name>
<a:Code>suivre_sommeil</a:Code>
<a:CreationDate>1767373444</a:CreationDate>
<a:Creator>houda</a:Creator>
<a:ModificationDate>1767373495</a:ModificationDate>
<a:Modifier>houda</a:Modifier>
</o:UseCase>
<o:UseCase Id="o126">
<a:ObjectID>088D4C35-0566-4115-B473-C3D9E28B6E33</a:ObjectID>
<a:Name>suivre hygiene</a:Name>
<a:Code>suivre_hygiene</a:Code>
<a:CreationDate>1767373446</a:CreationDate>
<a:Creator>houda</a:Creator>
<a:ModificationDate>1767373506</a:ModificationDate>
<a:Modifier>houda</a:Modifier>
</o:UseCase>
<o:UseCase Id="o127">
<a:ObjectID>8D1520A2-C36A-4567-9C0E-31B1BF3C4100</a:ObjectID>
<a:Name>Consulter historique repas</a:Name>
<a:Code>Consulter_historique_repas</a:Code>
<a:CreationDate>1767373518</a:CreationDate>
<a:Creator>houda</a:Creator>
<a:ModificationDate>1767373573</a:ModificationDate>
<a:Modifier>houda</a:Modifier>
</o:UseCase>
<o:UseCase Id="o128">
<a:ObjectID>C3A224AB-5447-42B3-A4A7-F1664FA65B71</a:ObjectID>
<a:Name>Ajouter heures sommeil</a:Name>
<a:Code>Ajouter_heures_sommeil</a:Code>
<a:CreationDate>1767373593</a:CreationDate>
<a:Creator>houda</a:Creator>
<a:ModificationDate>1767373627</a:ModificationDate>
<a:Modifier>houda</a:Modifier>
</o:UseCase>
<o:UseCase Id="o129">
<a:ObjectID>69D2EDF0-6E4F-40DF-AE6B-3098BB26264C</a:ObjectID>
<a:Name>Consulter historique sommeil</a:Name>
<a:Code>Consulter_historique_sommeil</a:Code>
<a:CreationDate>1767373594</a:CreationDate>
<a:Creator>houda</a:Creator>
<a:ModificationDate>1767373655</a:ModificationDate>
<a:Modifier>houda</a:Modifier>
</o:UseCase>
<o:UseCase Id="o130">
<a:ObjectID>D2DDB802-FBF3-446B-965D-CD407C61E724</a:ObjectID>
<a:Name>Ajouter changement de couche</a:Name>
<a:Code>Ajouter_changement_de_couche</a:Code>
<a:CreationDate>1767373695</a:CreationDate>
<a:Creator>houda</a:Creator>
<a:ModificationDate>1767373710</a:ModificationDate>
<a:Modifier>houda</a:Modifier>
</o:UseCase>
<o:UseCase Id="o131">
<a:ObjectID>19E37762-EFEC-4F54-A703-464DE2144A63</a:ObjectID>
<a:Name>Consulter historique de changement de couche</a:Name>
<a:Code>Consulter_historique_de_changement_de_couche</a:Code>
<a:CreationDate>1767373696</a:CreationDate>
<a:Creator>houda</a:Creator>
<a:ModificationDate>1767373728</a:ModificationDate>
<a:Modifier>houda</a:Modifier>
</o:UseCase>
<o:UseCase Id="o132">
<a:ObjectID>E61EE5CE-0CD1-486B-A6BF-F02331B13C7A</a:ObjectID>
<a:Name>Consulter des graphes de croissance</a:Name>
<a:Code>Consulter_des_graphes_de_croissance</a:Code>
<a:CreationDate>1767374157</a:CreationDate>
<a:Creator>houda</a:Creator>
<a:ModificationDate>1767374346</a:ModificationDate>
<a:Modifier>houda</a:Modifier>
</o:UseCase>
<o:UseCase Id="o133">
<a:ObjectID>57D55A36-C106-4D24-9BB8-B13E3A8CB7CA</a:ObjectID>
<a:Name>Consulter Courbe Poids / Âge</a:Name>
<a:Code>Consulter_Courbe_Poids___Age</a:Code>
<a:CreationDate>1767374168</a:CreationDate>
<a:Creator>houda</a:Creator>
<a:ModificationDate>1767374416</a:ModificationDate>
<a:Modifier>houda</a:Modifier>
</o:UseCase>
<o:UseCase Id="o134">
<a:ObjectID>56DCA8B6-8960-42FB-86E9-A3F52818D65B</a:ObjectID>
<a:Name>Consulter Courbe Taille / Âge</a:Name>
<a:Code>Consulter_Courbe_Taille___Age</a:Code>
<a:CreationDate>1767374169</a:CreationDate>
<a:Creator>houda</a:Creator>
<a:ModificationDate>1767374451</a:ModificationDate>
<a:Modifier>houda</a:Modifier>
</o:UseCase>
<o:UseCase Id="o135">
<a:ObjectID>09D9E72F-AE56-4936-A864-0739DB1FBACD</a:ObjectID>
<a:Name>Consulter Courbe Poids / Taille</a:Name>
<a:Code>Consulter_Courbe_Poids___Taille</a:Code>
<a:CreationDate>1767374171</a:CreationDate>
<a:Creator>houda</a:Creator>
<a:ModificationDate>1767374505</a:ModificationDate>
<a:Modifier>houda</a:Modifier>
</o:UseCase>
<o:UseCase Id="o136">
<a:ObjectID>1BE775F8-081E-4753-A56F-66797F37C8D3</a:ObjectID>
<a:Name>Consulter l&#39;IA</a:Name>
<a:Code>Consulter_l_IA</a:Code>
<a:CreationDate>1767374605</a:CreationDate>
<a:Creator>houda</a:Creator>
<a:ModificationDate>1767374623</a:ModificationDate>
<a:Modifier>houda</a:Modifier>
</o:UseCase>
<o:UseCase Id="o137">
<a:ObjectID>DC1F0031-9404-4770-BA85-9A11821004A3</a:ObjectID>
<a:Name>Consulter historique de conversations</a:Name>
<a:Code>Consulter_historique_de_conversations</a:Code>
<a:CreationDate>1767374606</a:CreationDate>
<a:Creator>houda</a:Creator>
<a:ModificationDate>1767374660</a:ModificationDate>
<a:Modifier>houda</a:Modifier>
</o:UseCase>
<o:UseCase Id="o138">
<a:ObjectID>3B584D76-F11A-4587-AA59-80C6BB5C7991</a:ObjectID>
<a:Name>poser question/demander aide</a:Name>
<a:Code>poser_question_demander_aide</a:Code>
<a:CreationDate>1767374607</a:CreationDate>
<a:Creator>houda</a:Creator>
<a:ModificationDate>1767374673</a:ModificationDate>
<a:Modifier>houda</a:Modifier>
</o:UseCase>
<o:UseCase Id="o140">
<a:ObjectID>5C02A9BB-97AB-4066-8C5D-48B08EA9338A</a:ObjectID>
<a:Name>Sychroniser entre appareils</a:Name>
<a:Code>Sychroniser_entre_appareils</a:Code>
<a:CreationDate>1767532797</a:CreationDate>
<a:Creator>houda</a:Creator>
<a:ModificationDate>1767532877</a:ModificationDate>
<a:Modifier>houda</a:Modifier>
</o:UseCase>
<o:UseCase Id="o141">
<a:ObjectID>041D9104-0B48-45BB-A836-78C894907F80</a:ObjectID>
<a:Name>Sauvgarder donnees</a:Name>
<a:Code>Sauvgarder_donnees</a:Code>
<a:CreationDate>1767532812</a:CreationDate>
<a:Creator>houda</a:Creator>
<a:ModificationDate>1767532892</a:ModificationDate>
<a:Modifier>houda</a:Modifier>
</o:UseCase>
<o:UseCase Id="o142">
<a:ObjectID>D14B7651-4C7C-4991-854B-C69DA92945B9</a:ObjectID>
<a:Name>Exporter donnees</a:Name>
<a:Code>Exporter_donnees</a:Code>
<a:CreationDate>1767532812</a:CreationDate>
<a:Creator>houda</a:Creator>
<a:ModificationDate>1767532947</a:ModificationDate>
<a:Modifier>houda</a:Modifier>
</o:UseCase>
</c:UseCases>
<c:UseCaseAssociations>
<o:UseCaseAssociation Id="o101">
<a:ObjectID>D24656C2-9E00-4946-92FB-5A9FF5DC50AE</a:ObjectID>
<a:Name>Association_1</a:Name>
<a:Code>Association_1</a:Code>
<a:CreationDate>1767375343</a:CreationDate>
<a:Creator>houda</a:Creator>
<a:ModificationDate>1767375343</a:ModificationDate>
<a:Modifier>houda</a:Modifier>
<c:Object1>
<o:UseCase Ref="o112"/>
</c:Object1>
<c:Object2>
<o:Actor Ref="o111"/>
</c:Object2>
</o:UseCaseAssociation>
<o:UseCaseAssociation Id="o103">
<a:ObjectID>F569241F-FC96-42F0-AE14-9B5DA44DDC1A</a:ObjectID>
<a:Name>Association_2</a:Name>
<a:Code>Association_2</a:Code>
<a:CreationDate>1767375345</a:CreationDate>
<a:Creator>houda</a:Creator>
<a:ModificationDate>1767375345</a:ModificationDate>
<a:Modifier>houda</a:Modifier>
<c:Object1>
<o:UseCase Ref="o116"/>
</c:Object1>
<c:Object2>
<o:Actor Ref="o111"/>
</c:Object2>
</o:UseCaseAssociation>
<o:UseCaseAssociation Id="o105">
<a:ObjectID>2C9884DB-B6CE-46FD-8815-CB44935599A8</a:ObjectID>
<a:Name>Association_3</a:Name>
<a:Code>Association_3</a:Code>
<a:CreationDate>1767375349</a:CreationDate>
<a:Creator>houda</a:Creator>
<a:ModificationDate>1767375349</a:ModificationDate>
<a:Modifier>houda</a:Modifier>
<c:Object1>
<o:UseCase Ref="o122"/>
</c:Object1>
<c:Object2>
<o:Actor Ref="o111"/>
</c:Object2>
</o:UseCaseAssociation>
<o:UseCaseAssociation Id="o107">
<a:ObjectID>A4C22B17-1AF6-427E-AB3A-D838CC6F0D17</a:ObjectID>
<a:Name>Association_4</a:Name>
<a:Code>Association_4</a:Code>
<a:CreationDate>1767375353</a:CreationDate>
<a:Creator>houda</a:Creator>
<a:ModificationDate>1767375353</a:ModificationDate>
<a:Modifier>houda</a:Modifier>
<c:Object1>
<o:UseCase Ref="o132"/>
</c:Object1>
<c:Object2>
<o:Actor Ref="o111"/>
</c:Object2>
</o:UseCaseAssociation>
<o:UseCaseAssociation Id="o109">
<a:ObjectID>2A01CDE2-6FB2-4355-A182-EFDBED38F12D</a:ObjectID>
<a:Name>Association_6</a:Name>
<a:Code>Association_6</a:Code>
<a:CreationDate>1767375365</a:CreationDate>
<a:Creator>houda</a:Creator>
<a:ModificationDate>1767375365</a:ModificationDate>
<a:Modifier>houda</a:Modifier>
<c:Object1>
<o:UseCase Ref="o136"/>
</c:Object1>
<c:Object2>
<o:Actor Ref="o111"/>
</c:Object2>
</o:UseCaseAssociation>
</c:UseCaseAssociations>
<c:TargetModels>
<o:TargetModel Id="o143">
<a:ObjectID>A95CCB44-342D-4ECF-8AAA-F10F78D98D4F</a:ObjectID>
<a:Name>Java</a:Name>
<a:Code>Java</a:Code>
<a:CreationDate>1767020302</a:CreationDate>
<a:Creator>houda</a:Creator>
<a:ModificationDate>1767476707</a:ModificationDate>
<a:Modifier>houda</a:Modifier>
<a:TargetModelURL>file:///%_OBJLANG%/java5-j2ee14.xol</a:TargetModelURL>
<a:TargetModelID>0DEDDB90-46E2-45A0-886E-411709DA0DC9</a:TargetModelID>
<a:TargetModelClassID>1811206C-1A4B-11D1-83D9-444553540000</a:TargetModelClassID>
<c:SessionShortcuts>
<o:Shortcut Ref="o3"/>
</c:SessionShortcuts>
</o:TargetModel>
<o:TargetModel Id="o144">
<a:ObjectID>27B4BF4B-9D97-4F9B-BCE4-420AB38764BD</a:ObjectID>
<a:Name>WSDL for Java</a:Name>
<a:Code>WSDLJava</a:Code>
<a:CreationDate>1767020303</a:CreationDate>
<a:Creator>houda</a:Creator>
<a:ModificationDate>1767476707</a:ModificationDate>
<a:Modifier>houda</a:Modifier>
<a:TargetModelURL>file:///%_XEM%/WSDLJ2EE.xem</a:TargetModelURL>
<a:TargetModelID>C8F5F7B2-CF9D-4E98-8301-959BB6E86C8A</a:TargetModelID>
<a:TargetModelClassID>186C8AC3-D3DC-11D3-881C-00508B03C75C</a:TargetModelClassID>
<c:SessionShortcuts>
<o:Shortcut Ref="o4"/>
</c:SessionShortcuts>
</o:TargetModel>
</c:TargetModels>
</o:Model>
</c:Children>
</o:RootObject>

</Model>