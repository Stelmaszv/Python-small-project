import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { BaseComponent } from './base/base.component';
import { AnqularStartComponent } from './anqular-start/anqular-start.component';
import { ListComponent } from './list/list.component'
import { CreateComponent } from './create/create.component';
const routes: Routes = [
  { path:'' , component:ListComponent},
  { path:'create' , component: CreateComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
export const routingComponents=[BaseComponent,AnqularStartComponent]
