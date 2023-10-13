Blockly.defineBlocksWithJsonArray([
    {
        "type": "take_off",
        "message0":"Take off",
        "previousStatement": null,
        "nextStatement": null,
        "colour": "#a10005"
    },
    {
        "type": "go_to",
        "message0":"Go to %1",
        "args0": [
            {
                "type": "field_input",
                "name": "LOCATION",
                "text": "location"
            }
        ],
        "previousStatement": null,
        "nextStatement": null,
        "colour": "#ff9100"
    },
    {
        "type": "take_picture",
        "message0":"Take a picture of %1",
        "args0": [
            {
                "type": "field_input",
                "name": "OBJECT",
                "text": "object"
            }
        ],
        "previousStatement": null,
        "nextStatement": null,
        "colour": "008c3a"
    },
    {
        "type": "land",
        "message0":"Land",
        "previousStatement": null,
        "nextStatement": null,
        "colour": "blue"
    },
])

const toolbox = {
    "kind": "flyoutToolbox",
    "contents": [
      {
        "kind": "block",
        "type": "take_off"
      },
      {
        "kind": "block",
        "type": "go_to"
      },
      {
        "kind": "block",
        "type": "take_picture"
      },
      {
        "kind": "block",
        "type": "land"
      },
    ]
}


const workspace = Blockly.inject('blocklyDiv', {
  media: './node_modules/blockly/media/',
  toolbox: toolbox,
  grid: {
      spacing: 20,
      length: 3,
      colour: '#ccc',
      snap: true
  },
  scrollbars: false
  });

const drone = new DroneController(workspace);

drone.takeoff();
drone.goto('Chick-Fil-A');
drone.takepicture('dumpster');
drone.land();