from SeeThru_Feeds.Model.Scripts.ScriptBase import ScriptBase
from SeeThru_Feeds.Model.Scripts.ScriptResult import ScriptResult
from SeeThru_Feeds.Model.Properties.Properties import FillableProperty, ResultProperty

class {{ Script_Name }}(ScriptBase):
		EXAMPLE_PROPERTY = FillableProperty(name="example_property", required=False)

		Script_Title="{{ Script_Name }}"

		# ------ Script Overrides ------
		def Script_Run(self): pass
		def Script_Evaluate(self, result):
			result.SetStatus("green")
			result.SetMessage("")