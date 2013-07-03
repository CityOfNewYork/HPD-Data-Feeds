<h1>HPD Data Feeds</h1>
<p>
Department of Housing Preservation and Development Data Feeds
As part of New York City's Open Data Policy, the Department of Housing Preservation and Development (HPD) posts or links to various data they collect in the course of doing business. Among other things, this will enable computer programmers and app builders to create applications and tools that could improve access to public information and put it at the fingertips of tenants, landlords, developers, elected officials, housing advocates, and other interested parties.   
Please note that HPD's information sets are generally large. The information files are in a standard XML format. The XML format is defined in schema files that accompany the information files. There is also a file explaining the information they provide and the schedule for new releases. For each information set HPD makes available, they distribute two zipped files. The first is a spreadsheet detailing what data they are making available and how that data is organized (schema files). The second file contains the information.  Data includes:  Building files, Charges files, Complaints files, Litigation files, Registration files, and Violation Files.
Note that public data sets made available on the web portal are provided for informational purposes. The City of New York does not warranty the completeness, accuracy, content or fitness for any particular purpose or use of any public data set made available on the web portal, nor are any such warranties to be implied or inferred with respect to the public data sets furnished therein. The City of New York is not liable for any deficiencies in the completeness, accuracy, content or fitness for any particular purpose or use of any public data set, or application utilizing such data set, provided by any third party.
</p>

<h1>Import The Library</h1>

<b>To use the included Python Library, you must first import it:</b><br />
<code>import HPD</code>

If the library fails to import, make sure python is set to search the directory that the file is located in. Then restart python and try again.


<h1>Creating the HPD Object</h1>

<b>Creating a HPD object and setting the API Key/ID:</b><br />
<code>myobj = HPD.HPD('API ID' , 'API Key') </code>


<b>Changing the API Key or ID for a HPD object that was already created: </b><br />
<code>
HPDObj.setID('NewID')<br />
HPDObj.setKey('NewKey')
</code>


<b>Getting the API Key or ID for a HPD object that was already created: </b><br />
<code>
HPDObj.getID() <br />
HPDObj.getKey()
</code>


<b> Get press releases from HPD using your object: </b><br />
<code>
pressReleases = HPD.getHPDFeed()
</code>


<b> To print the press releases in text format: </b><br />
<code>
print pressReleases.text
</code>

<b>For further documentation and examples, see the integrated help Doc in python:</b><br />
<code>help(HPD) </code>
