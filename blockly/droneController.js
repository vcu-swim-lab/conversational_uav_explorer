class DroneController {
    constructor(workspace) {
      this.workspace = workspace;
      this.commonXmlns = 'https://developers.google.com/blockly/xml';
    }
  
    executeBlocklyXml(xml) {
      Blockly.Xml.domToWorkspace(Blockly.utils.xml.textToDom(xml), this.workspace);
    }
  
    takeOff() {
      const xmlTakeOff = `<xml xmlns="${this.commonXmlns}"><block type="take_off"></block></xml>`;
      this.executeBlocklyXml(xmlTakeOff);
    }
  
    goTo(location) {
      const xmlGoTo = `<xml xmlns="${this.commonXmlns}">
        <block type="go_to">
          <field name="LOCATION">${location}</field>
        </block>
      </xml>`;
      this.executeBlocklyXml(xmlGoTo);
    }
  
    takePicture(object) {
      const xmlTakePicture = `<xml xmlns="${this.commonXmlns}">
          <block type="take_picture">
              <field name="OBJECT">${object}</field>
          </block>
      </xml>`;
      this.executeBlocklyXml(xmlTakePicture);
    }
  
    land() {
      const xmlLand = `<xml xmlns="${this.commonXmlns}"><block type="land"></block></xml>`;
      this.executeBlocklyXml(xmlLand);
    }
  }

