import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { BaseComponent } from './base/base.component';
import { AnqularStartComponent } from './anqular-start/anqular-start.component';
const routes: Routes = [
  { path:'AnqularStart' , component:AnqularStartComponent },
  { path:'' , component:BaseComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
export const routingComponents=[BaseComponent,AnqularStartComponent]
