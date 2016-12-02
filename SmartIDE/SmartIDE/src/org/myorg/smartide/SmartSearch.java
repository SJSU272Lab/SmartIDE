/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package org.myorg.smartide;

import java.awt.Component;
import java.awt.event.ActionEvent;
import javax.swing.AbstractAction;
import org.openide.awt.ActionID;
import org.openide.awt.ActionReference;
import org.openide.awt.ActionReferences;
import org.openide.awt.ActionRegistration;
import org.openide.util.NbBundle.Messages;
import org.openide.util.actions.Presenter;

@ActionID(
        category = "File",
        id = "org.myorg.smartide.SmartSearch"
)
@ActionRegistration(
        displayName = "#CTL_SmartSearch"
)
@ActionReferences({
    @ActionReference(path = "Menu/File", position = 0)
    ,
  @ActionReference(path = "Toolbars/File", position = 0)
})
@Messages("CTL_SmartSearch=Search")
public final class SmartSearch extends AbstractAction implements Presenter.Toolbar {

    @Override
    public Component getToolbarPresenter() {
        return new SearchPanel();
    }
    
    @Override
    public void actionPerformed(ActionEvent e) {
        // TODO implement action body
    }
}
