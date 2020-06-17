from SeeThru_Feeds.Model.Components.ComponentBase import ComponentBase
from SeeThru_Feeds.Model.Properties.Properties import FillableProperty, ResultProperty
import mysql.connector


class ConnectionOpen(ComponentBase):
    HOST = FillableProperty(name="Host", required=True)
    USER = FillableProperty(name="User", required=True)
    PASSWD = FillableProperty(name="password", required=True)
    DATABASE = FillableProperty(name="Database", required=True)
    CAN_CONNECT = ResultProperty(name="Can_Connect")

    Component_Title = "ConnectionOpen Database Component"
    Component_Description = "This component tests to see if it can open a database connection with the given details"
    Component_Author = "SeeThru Networks"
    Component_Owner = "SeeThru Networks"

    def Component_Execute(self):
        try:
            connection = mysql.connector.connect(
                host=self.GetProperty(ConnectionOpen.HOST),
                user=self.GetProperty(ConnectionOpen.USER),
                passwd=self.GetProperty(ConnectionOpen.PASSWD),
                database=self.GetProperty(ConnectionOpen.DATABASE)
            )
            connection.close()
            # Assumes that a valid connection was made
            self.SetProperty(ConnectionOpen.CAN_CONNECT, True)
        except:
            self.SetProperty(ConnectionOpen.CAN_CONNECT, False)
