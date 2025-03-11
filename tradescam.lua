loadstring(game:HttpGet(("https://raw.githubusercontent.com/daucobonhi/Ui-Redz-V2/refs/heads/main/UiREDzV2.lua")))()

       local Window = MakeWindow({
         Hub = {
         Title = "Trade Scam v3 new",
         Animation = "Script Trade scam 2025"
         },
        Key = {
        KeySystem = false,
        Title = "Key System",
        Description = "",
        KeyLink = "",
        Keys = {"1234"},
        Notifi = {
        Notifications = true,
        CorrectKey = "Running the Script...",
       Incorrectkey = "The key is incorrect",
       CopyKeyLink = "Copied to Clipboard"
      }
    }
  })

       MinimizeButton({
       Image = "http://www.roblox.com/asset/?id=128933802535491",
       Size = {60, 60},
       Color = Color3.fromRGB(10, 10, 10),
       Corner = true,
       Stroke = false,
       StrokeColor = Color3.fromRGB(255, 0, 0)
      })
      
------ Tab
     local Tab1o = MakeTab({Name = "MAIN"})
     
-------TOGGLE 

     Toggle = AddToggle(Tab1o, {
      Name = "don't jump",
      Default = false,
      Callback = function()
     end
    })
    
     Toggle = AddToggle(Tab1o, {
     Name = "Freeze Trade",
    Default = false,
      Callback = function()
  end
  })
      Toggle = AddToggle(Tab1o, {
     Name = "Auto Accept",
    Default = false,
      Callback = function()
end
  })
        Toggle = AddToggle(Tab1o, {
     Name = "Aouto Add Items",
    Default = false,
      Callback = function()
  end
  })
