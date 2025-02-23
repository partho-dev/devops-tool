import jenkins.model.Jenkins

def pm = Jenkins.instance.pluginManager
def uc = Jenkins.instance.updateCenter

// Check for plugin updates
pm.doCheckUpdatesServer()

// Plugins that are needed
def requiredPlugins = ["github", "kubernetes", "sonar", "ws-cleanup"]

requiredPlugins.each { pluginId ->
    if (!pm.getPlugin(pluginId)) {
        def plugin = uc.getPlugin(pluginId)
        if (plugin) {
            println "Installing plugin: ${pluginId}"
            def deployment = plugin.deploy(true) // Asynchronous deployment (true)
            deployment.get() // Wait for the plugin to be installed
        } else {
            println "Plugin not found in Update Center: ${pluginId}"
        }
    } else {
        println "Plugin ${pluginId} is already installed."
    }
}

// Restart Jenkins after plugin installation
println "Restarting Jenkins..."
Jenkins.instance.restart()

// After copying this script, paste it into the Jenkins UI under the "Script Console" (Manage Jenkins > Script Console)
// This will install all the necessary plugins listed above.
