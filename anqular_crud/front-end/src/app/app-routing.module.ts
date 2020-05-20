import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { BaseComponent } from './components/base/base.component';
import { AnqularStartComponent } from './components/anqular-start/anqular-start.component';
import { ListComponent } from './components/list/list.component'
import { CreateComponent } from './components/create/create.component';
import { GetComponent } from './components/get/get.component';
const routes: Routes = [
  { path:'' , component:ListComponent},
  { path:'create' , component: CreateComponent},
  { path:'list/:id' , component: GetComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
export const routingComponents=[BaseComponent,AnqularStartComponent]
